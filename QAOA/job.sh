#!/bin/bash
#SBATCH --job-name=job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p GPU-shared
#SBATCH --gpus=h100-80:1
##SBATCH --ntasks-per-node=2
#SBATCH -t 12:00:00             # Max time for the job
#SBATCH --output=cq_%j.out      # Standard output file

# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR

set -x

export SINGULARITY_CACHEDIR=$PWD/singularity_cache

export OMPI_MCA_opal_cuda_support=true
export OMPI_MCA_btl='^openib'

time -p singularity exec --cleanenv --nv --no-home /jet/home/nnepal/tests/cudaq_test/IQM/cuda-quantum.sif python3 maxcut.py
#time -p singularity exec --cleanenv --no-home /jet/home/nnepal/tests/cudaq_test/IQM/cuda-quantum.sif python3 iqm-maxcut.py
#time -p singularity exec --cleanenv --nv --no-home /jet/home/nnepal/tests/cudaq_test/IQM/cuda-quantum.sif python3 dc-qaoa.py
#singularity exec --cleanenv --nv --no-home /jet/home/nnepal/tests/cudaq_test/IQM/cuda-quantum.sif python3 adapt-qaoa.py
