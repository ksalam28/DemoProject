import os
import time


print("Starting Build Process")
os.system('minikube start --cpus 4 --memory 8192')
time.sleep(1)
os.system('kubectl apply -f elk/elasticsearch')
time.sleep(1)
os.system('kubectl apply -f elk/kibana')
time.sleep(1)
os.system('kubectl apply -f elk/beats_init')
time.sleep(1)
os.system('kubectl apply -f elk/beats_agents')
time.sleep(1)
os.system('kubectl apply -f app/app-deployment.yml')

print("Finished Build Process")

