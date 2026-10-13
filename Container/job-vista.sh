#!/bin/bash
#SBATCH -J job # Job name
#SBATCH -o job.o%j    # Name of stdout output file
#SBATCH -e job.e%j    # Name of stderr error file
#SBATCH -p gh         # Queue (partition) name
#SBATCH -N 1              # Total # of nodes
#SBATCH -n 1             # Total # of mpi tasks
#SBATCH -t 1:30:00       # Run time (hh:mm:ss)
#SBATCH -A DMR22013          # Project allocation

set -x

apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ghz_H.py > ghz_Hout
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python maxcut.py > maxcutout
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ghz.py > ghzout
##Downloading MNIST data
apptainer exec --cleanenv --nv --no-home python mnist_data.py
apptainer exec --cleanenv --nv --no-home cuda-quantum.sif python ml.py
apptainer exec --cleanenv --nv --no-home --bind $PWD/openfermion_data:/usr/local/lib/python3.12/dist-packages/openfermion/testing/data cuda-quantum.sif python vqe.py > vqeout
