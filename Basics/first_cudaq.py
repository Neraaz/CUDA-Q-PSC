import cudaq


# Define our kernel.
@cudaq.kernel
def kernel(qubit_count: int):
    # Allocate our qubits.
    qvector = cudaq.qvector(qubit_count)
    # Place the first qubit in the superposition state.
    h(qvector[0])
    # Loop through the allocated qubits and apply controlled-X,
    # or CNOT, operations between them.
    for qubit in range(qubit_count - 1):
        x.ctrl(qvector[qubit], qvector[qubit + 1])
    # Measure the qubits.
    mz(qvector)

if __name__ == "__main__":
    qubit_count = 2
    print(cudaq.draw(kernel, qubit_count))
    results = cudaq.sample(kernel, qubit_count)
    # Should see a roughly 50/50 distribution between the |00> and
    # |11> states. Example: {00: 505  11: 495}
    print("Measurement distribution:" + str(results))
