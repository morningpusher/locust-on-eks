# locust on AWS EKS

# helm
https://github.com/helm/charts/tree/master/stable/locust
- Not support for locust 1.0 as of August, 2020

- must change to command line parameter from env variables.
https://docs.locust.io/en/stable/running-locust-docker.html

- install
```
helm install locust --generate-name
```

- upgrade
```
helm upgrade $RELEASE_NAME locust
```

# kubectl
- portforward
```
kubectl port-forward $MASTER_POD_NAME 8089
```

# locust
https://github.com/locustio/locust/releases/tag/1.0
- version1.0
