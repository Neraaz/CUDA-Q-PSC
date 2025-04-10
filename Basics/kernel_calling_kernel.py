import cudaq


# Define our kernel.
@cudaq.kernel
def kernel_A(qubit_0: cudaq.qubit, qubit_1: cudaq.qubit):
    x.ctrl(qubit_0, qubit_1)

@cudaq.kernel
def kernel(qubit_count: int):
    # Allocate our qubits.
    qvector = cudaq.qvector(qubit_count)
    # Place the first qubit in the superposition state.

    for i in range(5):
        kernel_A(qvector[i], qvector[i + 1])

if __name__ == "__main__":
    qubit_count = 10
    print(cudaq.draw(kernel, qubit_count))
