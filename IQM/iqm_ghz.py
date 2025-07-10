# For single-gpu :
# python ghz.py --target nvidia
# For multi-threaded cpu :
# python ghz.py --target qpp-cpu
import os
import cudaq


os.environ["IQM_TOKENS_FILE"] = "/jet/home/nnepal/.resonance-api-token.json"
cudaq.set_target("iqm", 
                  url="https://cocos.resonance.meetiqm.com/garnet",
                  **{"qpu-architecture": "Apollo"})

def ghz_state(N):
    kernel = cudaq.make_kernel()
    q = kernel.qalloc(N)
    kernel.h(q[0])
    for i in range(N - 1):
      kernel.cx(q[i], q[i + 1])

    kernel.mz(q)
    return kernel

if __name__ == "__main__":
    n = 20
    print("Preparing GHZ state for", n, "qubits.")
    kernel = ghz_state(n)
    counts = cudaq.sample(kernel)
    print(counts)
