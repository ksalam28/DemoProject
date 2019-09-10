Demo Project (Jenkins, minikube, python)
----------------------------------------
Requirements: 
- Windows 10 (64bit)
- Jenkins for windows
- minikube for windows (requires: CPU=2, Memory=4096, disk-size=50GB)
- VirtualBox for windows (Hyper-V should be disabled)
- python 3.7.x

* kubeclt.exe path needs to be added in system env. variable
-------------------------------

Jenkinsfile: 
- pipeline config for jenkins job (build, test, deploy)
- please use this github repository for jenkins declarative pipeline (Jenkinsfile) 

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
