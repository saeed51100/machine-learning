### Commands:
```
set the pycharm terminal in your project folder.
```
```
conda create --prefix ./envs tensorflow-gpu numpy pandas scikit-learn
```

```
Set python interpreter to:  
/media/saeed/New Volume/repositories/machine-learning/jadi-course/envs/bin/python
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