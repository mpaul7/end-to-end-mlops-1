## MLOPS Project commands 


```shell
git init
git status
git add . 
git commit -m "add cookiecutter template"
git remote add origin https://github.com/mpaul7/end-to-end-mlops-1.git
git push origin master
pip install mlflow
pip install dagshub
pip install seaborn
pip install dvc
dvc init
dvc remote add -d myremote /home/mpaul/mlops-1
pip freeze > requirements.txt
```

```shell
https://github.com/mpaul7/end-to-end-mlops-1.git

https://dagshub.com/mpaul7/end-to-end-mlops-1.mlflow

import dagshub
dagshub.init(repo_owner='mpaul7', repo_name='end-to-end-mlops-1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
```