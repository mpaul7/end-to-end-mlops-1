import dagshub
dagshub.init(repo_owner='mpaul7', repo_name='end-to-end-mlops-1', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)