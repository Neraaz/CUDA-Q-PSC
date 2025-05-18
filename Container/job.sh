#!/bin/bash
#SBATCH --job-name=job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p RM
#SBATCH --ntasks-per-node=1
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

time -p singularity exec --cleanenv --no-home --bind $PWD/openfermion_data:/usr/local/lib/python3.10/dist-packages/openfermion/testing/data /ocean/projects/pscstaff/nnepal/containers/cuda-quantum.sif python3 vqe.py
