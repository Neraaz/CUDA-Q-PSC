import cudaq
from cudaq import spin
import numpy as np

hamiltonian = 5.907 - 2.1433 * spin.x(0) * spin.x(1) - 2.1433 * spin.y(
    0) * spin.y(1) + .21829 * spin.z(0) - 6.125 * spin.z(1)

@cudaq.kernel
def kernel(angles: list[float]):

    qubits = cudaq.qvector(2)
    x(qubits[0])
    ry(angles[0], qubits[1])
    x.ctrl(qubits[1], qubits[0])

#initial_params = np.random.normal(0, np.pi, 2)

optimizer = cudaq.optimizers.Adam()
gradient = cudaq.gradients.CentralDifference()


def objective_function(parameter_vector: list[float],
                       hamiltonian=hamiltonian,
                       gradient_strategy=gradient,
                       kernel=kernel) -> tuple[float, list[float]]:

        get_result = lambda parameter_vector: cudaq.observe(kernel, hamiltonian, parameter_vector).expectation()

        cost = get_result(parameter_vector)

        gradient_vector = gradient_strategy.compute(parameter_vector, get_result, cost)

        return cost, gradient_vector

energy, parameter = optimizer.optimize(dimensions=1,function=objective_function)

print(f"\nminimized <H> = {round(energy,16)}")
print(f"optimal theta 0 = {round(parameter[0],16)}")
