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


singularity build --fakeroot cuda-qx.sif cuda-qx.def
