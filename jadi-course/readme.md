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
     conda activate ./envs
     conda activate ./bade
     conda deactivate
---

```
for remove environments:
first deactivate all environments check:
conda env list
then:
conda env remove --prefix ./envs
if not remove completelly you should remove folder manually:
sudo rm -rf envs
```
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