#Run basic quantum circuit on IQM
Build CUDA-Q container
sbatch build.sh

echo "{ \"access_token\": \"${IQM_TOKEN}\" }" > .resonance-api-token.json

IQM_TOKEN can be generated from IQM Resonance Quantum Cloud Platform.

singularity exec --cleanenv --nv --no-home /jet/home/nnepal/tests/cudaq_test/IQM/cuda-quantum.sif python3 iqm_sampl
e.py

Results:
{ 00000:440 00001:5 00010:25 00011:2 00100:16 00110:2 01000:2 10000:32 10010:438 10011:3 10110:27 10111:2 11000:1 11010:5 }

{ 00000:472 00001:6 00010:13 00011:1 00100:12 00110:3 01000:1 10000:32 10010:424 10011:8 10100:2 10110:19 11000:1 11010:6 }

More detail results can be found via Cloud Platform. Just Go to Job and click the one you interested to look at.
