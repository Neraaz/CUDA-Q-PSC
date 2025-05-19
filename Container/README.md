---

# Using the `cuda-quantum.sif` Container for VQE Simulations

## 1. Build the Container

Submit the batch job to build the `.sif` container:

```bash
sbatch build.sh
```

Once the job completes, a Singularity image file (`cuda-quantum.sif`) will be created in your working directory.

---

## 2. Start an Interactive Session

Launch an interactive session:

```bash
interact
```

Then, start a clean Apptainer shell inside the container:

```bash
apptainer shell --cleanenv --no-home cuda-quantum.sif
```

> **Note**: Using `--cleanenv` and `--no-home` ensures the shell does not inherit your existing Python or system environment, keeping the containerized environment isolated and reproducible.

---

## 3. Explore the Python Environment

Start an interactive Python session:

```bash
ipython
```

You can verify module paths and versions. For example:

```python
import numpy
numpy.__path__
numpy.__version__
```

Confirm that the module is being loaded from within the container environment.

---

## 4. Portability of the Container

The `.sif` file is self-contained. You can copy or move it to any folder, and it will remain usable on supported systems.

---

## 5. Run a VQE Job

To run a job using the container (e.g., computing the ground-state energy of H2 molecule), submit a job script:

```bash
sbatch job.sh
```
Make sure you change `/ocean/projects/pscstaff/nnepal/containers/cuda-quantum.sif` with path where you have `cuda-quantum.sif`.

---
