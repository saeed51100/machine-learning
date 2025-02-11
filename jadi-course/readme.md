### Commands:
```
conda env create --prefix ./envs -f environment.yml
```
```
conda env update -f environment.yml --prune
```
```
Set python interpreter to:  
/media/saeed/New Volume/repositories/machine-learning/jadi-course/envs/bin/python3.12
```

---
     Only if needed for terminal work: (Usually not needed in PyCharm.)
     conda activate ./envs
     conda deactivate
---
```
conda list
```
```
conda env list
```
```
conda info --envs
```
---
```
conda remove --name myenv --all
```