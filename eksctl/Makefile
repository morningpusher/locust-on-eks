CLUSTER_NAME:=basic-cluster
REGION:=us-east-2

setup:
	# eksctl
	# https://eksctl.io/
	@curl --silent --location "https://github.com/weaveworks/eksctl/releases/download/latest_release/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
	@sudo mv /tmp/eksctl /usr/local/bin

setup/minikube/prometheus:
	minikube addons enable ingress
	minikube config set memory 8192
	minikube config set cpus 4
	minikube config set disk-size 40g

setup/j2cli:
	pip install j2cli


# echo `minikube ip` k8s.3tier.webapp alertmanager.minikube prometheus.minikube grafana.minikube >> /etc/hosts

start/minikube:
	minikube start \
		--extra-config=kubelet.authentication-token-webhook=true \
		--extra-config=kubelet.authorization-mode=Webhook \
		--extra-config=apiserver.Authorization.Mode=RBAC

eksctl/create/cluster:
	eksctl create cluster -f config.yaml

eksctl/create/nodegroup:
	eksctl create nodegroup -f config.yaml

eksctl/upgrade/nodegroup:
	eksctl upgrade nodegroup -f config.yaml --cluster $(CLUSTER_NAME)

eksctl/create/isa:
	eksctl create iamserviceaccount -f config.yaml --override-existing-serviceaccounts --approve

eksctl/delete/isa:
	eksctl delete iamserviceaccount -f config.yaml --approve

eksctl/update/cluster:
	eksctl upgrade cluster -f config.yaml

eksctl/create/nodegroup:
	eksctl create nodegroup -f config.yaml

eksctl/delete/cluster:
	eksctl delete cluster -f config.yaml

update/eksconfig:
	aws eks update-kubeconfig --name $(CLUSTER_NAME) --region $(REGION)

eksctl/utils/associate-iam-oidc:
	eksctl utils associate-iam-oidc-provider --region=$(REGION) --cluster=$(CLUSTER_NAME) --approve

help: ## print this message
	@echo "kubernetes operations by make."
	@echo ""
	@echo "Usage: make SUB_COMMAND "
	@echo ""
	@echo "Command list:"
	@echo ""
	@printf "\033[36m%-30s\033[0m %-50s %s\n" "[Sub command]" "[Description]" "[Example]"
	@grep -E '^[/a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | perl -pe 's%^([/a-zA-Z_-]+):.*?(##)%$$1 $$2%' | awk -F " *?## *?" '{printf "\033[36m%-30s\033[0m %-50s %s\n", $$1, $$2, $$3}'
