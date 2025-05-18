Usage:
sbatch job.sh <script_name>

For example:
sbatch job.sh first_cudaq.py

Output can be checked in cq_<job_id>.out files

Here are the lists
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh first_cudaq.py 
Submitted batch job 31447285
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh second_cudaq.py 
Submitted batch job 31447289
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh third_cudaq.py 
Submitted batch job 31447290
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh control_qubit.py 
Submitted batch job 31447291
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh custom_gate.py 
Submitted batch job 31447292
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh ghz.py 
Submitted batch job 31447293
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh kernel_calling_kernel.py 
Submitted batch job 31447294
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh measure_1.py 
Submitted batch job 31447295
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh mid-circuit.py 
Submitted batch job 31447296
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh optimizer.py 
Submitted batch job 31447297
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh practice.py 
Submitted batch job 31447302
(base) [nnepal@bridges2-login013 CPU]$ sbatch job.sh target.py 
Submitted batch job 31447305

