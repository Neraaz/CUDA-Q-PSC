import openfermion
import openfermionpyscf
from openfermion.transforms import jordan_wigner, get_fermion_operator

import os
import timeit

import cudaq
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import numpy as np
import sys


@cudaq.kernel
def kernel(qubit_num: int, electron_num: int, thetas: list[float]):
    qubits = cudaq.qvector(qubit_num)

    for i in range(electron_num):
        x(qubits[i])

    cudaq.kernels.uccsd(qubits, thetas, electron_num, qubit_num)



def batched_gradient_function(kernel, parameters, hamiltonian, epsilon):

    x = np.tile(parameters, (len(parameters), 1))

    xplus = x + (np.eye(x.shape[0]) * epsilon)

    xminus = x - (np.eye(x.shape[0]) * epsilon)

    g_plus = []
    g_minus = []
    gradients = []

    qpu_counter = 0  # Iterate over the number of GPU resources available
    for i in range(x.shape[0]):

        g_plus.append(
            cudaq.observe_async(kernel,
                                hamiltonian,
                                qubit_count,
                                electron_count,
                                xplus[i],
                                qpu_id=qpu_counter%num_qpus))
        qpu_counter += 1

        g_minus.append(
            cudaq.observe_async(kernel,
                                hamiltonian,
                                qubit_count,
                                electron_count,
                                xminus[i],
                                qpu_id=qpu_counter%num_qpus))
        qpu_counter += 1

    gradients = [
        (g_plus[i].get().expectation() - g_minus[i].get().expectation()) /
        (2 * epsilon) for i in range(len(g_minus))
    ]

    assert len(gradients) == len(
        parameters) == x.shape[0] == xplus.shape[0] == xminus.shape[0]

    return gradients



if __name__ == "__main__":
    elem1 = "Na"
    elem2 = "H"
    d = 1.88
    geometry = [(elem1, (0, 0, 0)), (elem2, (0, 0, d))]
    basis = 'sto3g'
    multiplicity = 1
    charge = 0
    
    molecule = openfermionpyscf.run_pyscf(
        openfermion.MolecularData(geometry, basis, multiplicity, charge))
    
    molecular_hamiltonian = molecule.get_molecular_hamiltonian()
    
    fermion_hamiltonian = get_fermion_operator(molecular_hamiltonian)
    
    qubit_hamiltonian = jordan_wigner(fermion_hamiltonian)
    
    spin_ham = cudaq.SpinOperator(qubit_hamiltonian)
    electron_count = molecule.n_electrons
    qubit_count = 2 * molecule.n_orbitals
    np.random.seed(42)
    parameter_count = cudaq.kernels.uccsd_num_parameters(electron_count,
                                                         qubit_count)
    init_params = np.random.normal(0, 1, parameter_count)
    
    cudaq.set_target('nvidia',option='mgpu')
    
    num_qpus = cudaq.get_target().num_qpus()
    print(f"GPUs: {num_qpus}", flush=True)
    
    epsilon = np.pi / 4

    gradient = batched_gradient_function(kernel, init_params, spin_ham, epsilon)
    
    exp_vals = []
    
    def objective_function(parameter_vector: list[float], \
                           gradient=gradient, hamiltonian=spin_ham, kernel=kernel):
    
        get_result = lambda parameter_vector: cudaq.observe\
            (kernel, hamiltonian, qubit_count, electron_count, parameter_vector).expectation()
    
        cost = get_result(parameter_vector)
        exp_vals.append(cost)
        gradient_vector = batched_gradient_function(kernel, parameter_vector,
                                                    spin_ham, epsilon)
        print(f"Energy: {cost}", flush=True)
    
        return cost, gradient_vector
    
    start_time = timeit.default_timer()
    result_vqe = minimize(objective_function,
                          init_params,
                          method='CG',
                          jac=True,
                          tol=1e-6,
                          options={'maxiter': 1})
    end_time = timeit.default_timer()
    
    print('VQE-UCCSD energy= ', result_vqe.fun)
    print('Total elapsed time (s) = ', end_time - start_time)
    
    plt.plot(exp_vals)
    plt.xlabel('Epochs')
    plt.ylabel('Energy')
    plt.title('VQE')
    plt.savefig('vqe2.png')
