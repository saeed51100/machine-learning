###  Why included conda-forge in environment.yml?

* **TensorFlow with/without CUDA:** This is the most important reason to include conda-forge in environment.yml.  conda-forge provides TensorFlow builds that are specifically compiled for CUDA (e.g., tensorflow-gpu) and also CPU-only builds (tensorflow).


* **CUDA Machine:** On your machine with CUDA, conda will automatically install the CUDA-enabled TensorFlow build when you just specify tensorflow. You don't need to specify tensorflow[and-cuda] explicitly; conda will handle that for you.  Make sure you have the correct CUDA drivers and toolkit installed on your system.


* **Non-CUDA Machine:** On your machine without CUDA, conda will automatically install the CPU-only version of TensorFlow when you specify tensorflow.  Again, you don't need to do anything special.


* **Consistency:** Using conda-forge ensures that both your development and deployment environments remain consistent, regardless of the hardware differences between your machines.

* **Future Flexibility:** If you need to add more packages in the future (or adjust for specific CUDA versions), the conda-forge ecosystem typically provides a flexible and up-to-date collection.

### Useful commands:
```
conda env create -f environment.yml
conda env update -f environment.yml
conda activate myenv

conda list
conda env list
conda info --envs

conda deactivate
```