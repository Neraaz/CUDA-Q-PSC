import cudaq
import numpy as np

cudaq.register_operation("custom_x", np.array([0,1,1,0]))

# Define our kernel.
@cudaq.kernel
def kernel():
    qvector = cudaq.qvector(2)
    h(qvector[0])
    custom_x(qvector[0])
    custom_x.ctrl(qvector[0], qvector[1])
    mz(qvector)



if __name__ == "__main__":
    results = cudaq.sample(kernel)
    print(results)
    print(cudaq.draw(kernel))
    # Should see a roughly 50/50 distribution between the |00> and
    # |11> states. Example: {00: 505  11: 495}
    print("Measurement distribution:" + str(results))
