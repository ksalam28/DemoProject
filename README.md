Demo Project (Jenkins, minikube, python)
----------------------------------------
Requirements: 
- Windows 10 (64bit)
- Jenkins for windows
- minikube for windows (requires: CPU=2, Memory=4096, disk-size=50GB)
- VirtualBox for windows (Hyper-V should be disabled, visualization must be enabled from BIOS)
- python 3.7.x

* kubeclt.exe path needs to be added in system env. variable (https://github.com/Azure/azure-cli/issues/5374 may help to configure)
-------------------------------

Jenkins: 
- pipeline config groovy for jenkins job (build, test, deploy)
- please use this github repository for jenkins declarative pipeline (Jenkinsfile groovy file) 

Manual Build:
- minikube start --cpus 2 --memory 4096 --disk-size 50GB
- minikube dashboard
- kubectl apply -f elk/elasticsearch
- kubectl apply -f elk/kibana
- kubectl apply -f elk/beats_init
- kubectl apply -f elk/beats_agents
- kubectl apply -f app/app-deployment.yml
- kubectl port-forward service/flask-app 5000
- python test.py
-----------------------------

app: 
- python flask app with docker configuration file.
- Docker image: ksalam28/flask-demo:latest
- contains manifest of flask-app (kubernetes)
     
elk: 
- contains manifest of
- elasticsearch
- kibana
- filebeat

test: 
- infrastructure test using python kubetest 
- flask app test in python (functional test)
- integration test using python kubetest



