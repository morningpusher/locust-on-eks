CLUSTER_NAME:=kubeflow-cluster
REGION:=us-east-2

# https://github.com/kubeflow/kfctl/releases/tag/v1.0.2
setup/locust:
	@helm pull stable/locust --version 1.2.1
