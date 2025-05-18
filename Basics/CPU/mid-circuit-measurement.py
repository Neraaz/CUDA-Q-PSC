import cudaq

@cudaq.kernel
def kernel():
    q = cudaq.qvector(2)
    h(q[0])
    b0 = mz(q[0])
    reset(q[0])
    x(q[0])

    if b0:
        h(q[1])

if __name__ == "__main__":
    print(cudaq.draw(kernel))
    print(cudaq.sample(kernel))
