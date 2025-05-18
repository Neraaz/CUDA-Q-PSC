import cudaq


# Define our kernel.
@cudaq.kernel
def kernel():
    qvector = cudaq.qvector(3)
    x(qvector)
    x(qvector[1])
    x.ctrl([qvector[0], qvector[1]], qvector[2])
    mz(qvector)



if __name__ == "__main__":
    results = cudaq.sample(kernel)
    print(results)
    print(cudaq.draw(kernel))
    # Should see a roughly 50/50 distribution between the |00> and
    # |11> states. Example: {00: 505  11: 495}
    print("Measurement distribution:" + str(results))
