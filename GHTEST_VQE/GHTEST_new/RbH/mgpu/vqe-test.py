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

def vqe(elem1,elem2,d):
    global rank
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
    
    @cudaq.kernel
    def kernel(qubit_num: int, electron_num: int, thetas: list[float]):
        qubits = cudaq.qvector(qubit_num)
    
        for i in range(electron_num):
            x(qubits[i])
    
        cudaq.kernels.uccsd(qubits, thetas, electron_num, qubit_num)
    
    
    parameter_count = cudaq.kernels.uccsd_num_parameters(electron_count,
                                                         qubit_count)
    if rank == 0:
        print(f"electrons: {electron_count}, qubit count: {qubit_count}, parameters: {parameter_count}")
    
    def cost(theta):
    
        exp_val = cudaq.observe(kernel, spin_ham, qubit_count, electron_count,
                                theta).expectation()
    
        return exp_val
    
    
    exp_vals = []
    
    
    counter = {'n': 0}
    def callback(xk):
        energy = cost(xk)
        exp_vals.append(energy)
        counter['n'] += 1
        if rank == 0:
            print(f"Iteration {counter['n']}:{energy}", flush=True)
    
    # Initial variational parameters.
    np.random.seed(42)
    x0 = np.random.normal(0, 1, parameter_count)
    
    start_time = timeit.default_timer()
    result = minimize(cost,
                      x0,
                      method='COBYLA',
                      callback=callback,
                      tol=1e-6,
                      options={'maxiter': 10})
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    deltae = exp_vals[-1] - exp_vals[-2]
    if rank == 0:
        print(f"Epochs: {len(exp_vals)}, del_e: {deltae}, time={total_time}")
        plt.plot(exp_vals)
        plt.xlabel('Epochs')
        plt.ylabel('Energy')
        plt.title('VQE')
        plt.savefig(f"vqe-{d}.png")
    return d,min(exp_vals),total_time
if __name__ == "__main__":
    cudaq.set_target('nvidia',option='mgpu')
    rank = 0
    elem1 = "Rb"
    elem2 = "H"
    distance = 2.40
    d,e0,time=vqe(elem1,elem2,distance)
    if rank == 0:
        with open(f"result.csv", "w") as write_csv:
            write_csv.write(str(d) + "," + str(e0) + "," + str(time) + "\n")
