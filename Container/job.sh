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

apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ghz_H.py > ghz_Hout
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python maxcut.py > maxcutout
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ghz.py > ghzout
##Downloading MNIST data
python mnist_data.py
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ml.py
apptainer exec --cleanenv --nv --no-home --bind $PWD/openfermion_data:/usr/local/lib/python3.12/dist-packages/openfermion/testing/data cuda-quantum.sif python vqe.py > vqeout
