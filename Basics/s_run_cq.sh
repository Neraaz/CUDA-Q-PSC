#!/bin/bash
#SBATCH --job-name=job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p GPU-shared
#SBATCH --gpus=h100-80:1
#SBATCH -t 01:00:00             # Max time for the job
#SBATCH --output=cq_%j.out      # Standard output file

# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR

set -x
module load anaconda3
export AAU_TOKEN_PATH=/ocean/projects/pscstaff/nnepal/conda/aau_token
export CONDARC=/jet/home/nnepal/.condarc
export CONDA_ENVS_DIRS=/ocean/projects/pscstaff/nnepal/conda/envs
export CONDA_PKGS_DIRS=/ocean/projects/pscstaff/nnepal/conda/pkgs

source activate cudaq-env
#Setting variable for CUDAQ
export PYTHONPATH="/ocean/projects/pscstaff/nnepal/conda/envs/cudaq-env/lib/python3.12/site-packages:$PYTHONPATH"
export OMPI_MCA_opal_cuda_support=true OMPI_MCA_btl='^openib'
export LD_LIBRARY_PATH="/ocean/projects/pscstaff/nnepal/conda/envs/cudaq-env/lib:$LD_LIBRARY_PATH"
export MPI_PATH=/ocean/projects/pscstaff/nnepal/conda/envs/cudaq-env

time -p python3 optimizer.py --target nvidia
#time -p python3 mid-circuit.py --target nvidia
#time -p python3 custom_gate.py --target nvidia
#time -p python3 control_qubit.py --target nvidia
#time -p python3 kernel_calling_kernel.py --target nvidia
#time -p mpirun -np 4 python3 parcir.py --target nvidia --target-option mgpu
#time -p mpirun -np 2 python3 mid-circuit.py --target nvidia --target-option mgpu
