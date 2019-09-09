import os
import time


print("Starting Deploy Process")
os.system('minikube stop')
time.sleep(1)
os.system('minikube delete')

print("Finished Deploy Process")

