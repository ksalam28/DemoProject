import os
import time


print("Starting Build Process")
#os.system('minikube start --cpus 2 --memory 4096 --disk-size 50GB')
time.sleep(1)
#os.system('minikube dashboard') # blocking command
time.sleep(1)
os.system('kubectl apply -f elk/elasticsearch')
time.sleep(3)
os.system('kubectl apply -f elk/kibana')
time.sleep(3)
#os.system('kubectl apply -f elk/beats_init')
#time.sleep(3)
os.system('kubectl apply -f elk/beats_agents')
time.sleep(3)
os.system('kubectl apply -f app/app-deployment.yml')

print("Waiting for 300 sec .......")
time.sleep(300)

print("Finished Build Process")

