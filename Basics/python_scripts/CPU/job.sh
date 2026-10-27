#!/bin/bash
#SBATCH --job-name=job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p RM
#SBATCH --ntasks-per-node=1
#SBATCH -t 1:00:00             # Max time for the job
#SBATCH --output=cq_%j.out      # Standard output file

# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR

set -x

export SINGULARITY_CACHEDIR=$PWD/singularity_cache

export OMPI_MCA_opal_cuda_support=true
export OMPI_MCA_btl='^openib'

time -p singularity exec --cleanenv --no-home /ocean/projects/pscstaff/nnepal/containers/cuda-quantum.sif python3 $1
