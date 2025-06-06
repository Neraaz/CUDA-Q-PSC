#!/bin/bash
#SBATCH --job-name=job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p GPU-shared
#SBATCH --gpus=h100-80:2
#SBATCH --ntasks-per-node=2
#SBATCH -t 12:00:00             # Max time for the job
#SBATCH --output=cq_%j.out      # Standard output file

# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR

set -x

export SINGULARITY_CACHEDIR=$PWD/singularity_cache
export OPENFERMION_DATA_DIRECTORY=$PWD/openfermion_data
mkdir -p "$OPENFERMION_DATA_DIRECTORY"

export OMPI_MCA_opal_cuda_support=true
export OMPI_MCA_btl='^openib'

singularity exec --cleanenv --nv --no-home --bind $PWD/openfermion_data:/usr/local/lib/python3.10/dist-packages/openfermion/testing/data /jet/home/nnepal/tests/cudaq_test/GHTEST_1/cuda-quantum.sif mpiexec -np 2 python3 vqe.py
