Demo Project (Jenkins, minikube, python)
----------------------------------------
Requirements: 
- Windows 10 (64bit)
- Jenkins for windows
- minikube for windows
- python 3.7.x
               
jenkinsfile: pipeline config for jenkins job (build, test, deploy)
             please use this github repository for jenkins declarative pipeline (jenkinsfile) 


app: python flask app with docker configuration file.
     docker image: ksalam28/flask-demo:latest
     
elk: contains manifest file for kubernetes (elasticsearch, kibana, filebeat, filemetric)

test: contains kubernetes test and python flask app test in python
