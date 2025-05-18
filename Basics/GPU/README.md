Usage:
sbatch job-gpu.sh <script_name>

For example:
sbatch job-gpu.sh first_cudaq.py

Output can be checked in cq_<job_id>.out files

Here are the lists
(base) [nnepal@bridges2-login013 GPU]$ sbatch job-gpu.sh expectation.py 
Submitted batch job 31447728
(base) [nnepal@bridges2-login013 GPU]$ sbatch job-gpu.sh parcir.py 
Submitted batch job 31447731

