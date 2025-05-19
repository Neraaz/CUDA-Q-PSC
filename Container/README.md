---

# Using the `cuda-quantum.sif` Container for VQE Simulations

## 1. Build the Container

Submit the batch job to build the `.sif` container:

```bash
sbatch build.sh
```

Once the job completes, a Singularity image file (`cuda-quantum.sif`) will be created in your working directory.

Here is the polished content formatted as a `README.md` section:

## Building for ARM64 Architecture

Currently, the `cuda-quantum.def` file uses the following base image:

```

nvcr.io/nvidia/nightly/cuda-quantum:cu12-latest

````

This tag typically resolves to the Docker image for the `x86_64` architecture. To build the container for the `ARM64` architecture (e.g., for Grace Hopper systems), you must specify the platform-specific image digest.

### ✅ Steps

1. Replace the image tag in your `cuda-quantum.def` file with the appropriate digest reference. For example:

    ```bash
    nvcr.io/nvidia/nightly/cuda-quantum@sha256:81a5ad82560e8e3015b33792df6fd0a53a21e5d763901ca72e411011a4435e4e
    ```

2. This ensures Singularity or Apptainer pulls the correct ARM64 variant of the image and avoids platform mismatch errors.

### 🔍 How to Find the Correct ARM64 Digest

1. Visit the [CUDA Quantum NGC Container Tags page](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nightly/containers/cuda-quantum/tags).

2. Click on any image tag (e.g., `cu12-latest`) to expand its details.

3. Look for the **“Digest”** section under each architecture (such as `linux/arm64`).

4. Copy the full digest string starting with `sha256:` and use it in your `.def` file as shown above.

---

With this change, you’ll be able to build the container successfully for ARM64 platforms.

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
