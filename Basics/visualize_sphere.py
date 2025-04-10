import cudaq
import numpy as np

## Retry the subsequent cells by setting the target to density matrix simulator.
# cudaq.set_target("density-matrix-cpu")


@cudaq.kernel
def kernel(angles: np.ndarray):
    qubit = cudaq.qubit()
    rz(angles[0], qubit)
    rx(angles[1], qubit)
    rz(angles[2], qubit)

if __name__ == "__main__":
    rng = np.random.default_rng(seed=11)
    blochSphereList = []
    for _ in range(4):
        angleList = rng.random(3) * 2 * np.pi
        sph = cudaq.add_to_bloch_sphere(cudaq.get_state(kernel, angleList))
        blochSphereList.append(sph)
    cudaq.show(blochSphereList[:], nrows=2, ncols=2)
    print(cudaq.show(blochSphereList[:], nrows=2, ncols=2))
