#!/bin/bash
#SBATCH -J job # Job name
#SBATCH -o job.o%j    # Name of stdout output file
#SBATCH -e job.e%j    # Name of stderr error file
#SBATCH -p gg         # Queue (partition) name
#SBATCH -N 1              # Total # of nodes
#SBATCH -t 00:30:00       # Run time (hh:mm:ss)
#SBATCH -A DMR22013          # Project allocation
# Set up the environment
#module load singularity
#cd $SLURM_SUBMIT_DIR

module load tacc-apptainer/1.3.3
singularity build --fakeroot cuda-quantum.sif cuda-quantum.def
