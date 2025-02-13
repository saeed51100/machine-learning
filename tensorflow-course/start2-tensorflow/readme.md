### Commands:
```
set the pycharm terminal in your project folder.
```
```
Set pycharm interpreter to base:  
/home/saeed/miniconda3/bin/python
```
```
conda activate base
```
```
conda create --prefix ./envs tensorflow-gpu numpy pandas scikit-learn
```

```
Set pycharm interpreter to:  
./envs/bin/python
```

---
     conda activate ./envs
     conda activate bade
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