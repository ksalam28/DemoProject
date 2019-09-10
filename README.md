Demo Project (Jenkins, minikube, python)
----------------------------------------
Requirements: 
- Windows 10 (64bit)
- Jenkins for windows
- minikube for windows (requires: CPU=2, Memory=4096, disk-size=50GB)
- VirtualBox for windows (Hyper-V should be disabled)
- python 3.7.x
-------------------------------

Jenkinsfile: 
- pipeline config for jenkins job (build, test, deploy)
- please use this github repository for jenkins declarative pipeline (Jenkinsfile) 

app: 
- python flask app with docker configuration file.
- Docker image: ksalam28/flask-demo:latest
     
elk: 
- contains manifest of
- elasticsearch
- kibana
- filebeat

test: 
- contains pytho kubernetes 
- flask app test in python
