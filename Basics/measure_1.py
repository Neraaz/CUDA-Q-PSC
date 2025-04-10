import cudaq

@cudaq.kernel
def kernel():
    qubits = cudaq.qvector(2)
    mx(qubits)
    mz()

if __name__ == "__main__":
    print(cudaq.draw(kernel))
    print(cudaq.sample(kernel))
