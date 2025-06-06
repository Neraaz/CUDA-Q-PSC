#!/bin/bash
#SBATCH -J job # Job name
#SBATCH -o job.o%j    # Name of stdout output file
#SBATCH -e job.e%j    # Name of stderr error file
#SBATCH -p gh         # Queue (partition) name
#SBATCH -N 2              # Total # of nodes
#SBATCH -t 03:00:00       # Run time (hh:mm:ss)
#SBATCH -A DMR22013          # Project allocation
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
