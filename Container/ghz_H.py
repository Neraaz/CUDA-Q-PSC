import cudaq
from cudaq import spin
import timeit

# Define a quantum kernel that returns an integer
@cudaq.kernel
def ghz_kernel(qubit_count: int):
    # Allocate qubits
    qubits = cudaq.qvector(qubit_count)

    # Create GHZ state
    h(qubits[0])
    for i in range(1, qubit_count):
        x.ctrl(qubits[0], qubits[i])

def z_power_n(n: int):
    if n <= 0:
        raise ValueError("n must be >= 1")
    op = spin.z(0)           # start with Z on qubit 0
    for i in range(1, n):    # multiply to form tensor product Z(0)*Z(1)*...*Z(n-1)
        op = op * spin.z(i)
    return op

if __name__ == "__main__":
    #Uncomment different sections for different backends

    #CPU only backend
    #cudaq.set_target('qpp-cpu')

    #Single GPU backend
    #cudaq.set_target('nvidia')

    #Multi-GPU backend
    #cudaq.set_target('nvidia', option='mgpu')
    #Run in 2 GPUs with "mpirun -np 2 python ghz.py > out &

    #Multi-QPU backend
    cudaq.set_target('nvidia')

    #Initialize MPI for execution=cudaq.parallel.mpi

    #Change qubit count
    qubit_count = 31
    
    #Draw circuit
    #print(cudaq.draw(ghz_kernel, qubit_count))
    

    #Our Hamiltonian
    h_op = z_power_n(qubit_count)
    #Compute Expectation value
    start_time = timeit.default_timer()
    #1 QPU
    #results = cudaq.observe(ghz_kernel, h_op, qubit_count).expectation()
    #2 QPU
    results = cudaq.observe(ghz_kernel, h_op, qubit_count).expectation()
    end_time = timeit.default_timer()
    total_time = end_time - start_time
    
    #Print results
    print(f"Results: {results}, time: {total_time}")
    # MPI finalize if it was initialized.
