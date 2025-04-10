#!/bin/bash
#SBATCH --job-name=qe-job       # Job name
#SBATCH -N 1 # Number of nodes
#SBATCH -p RM-shared
#SBATCH --ntasks-per-node=1
#SBATCH -t 00:10:00             # Max time for the job

# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR
module load intel-oneapi

export OMP_NUM_THREADS=64

set -x
./a.out
./new
