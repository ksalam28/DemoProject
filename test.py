import os
import time


print("Starting Test Process")
os.system('pip install -r test-requirements.txt')
time.sleep(1)
print("Kubernetes Infrastructure Test")
os.system('python test/kubernetes_test.py')
time.sleep(1)
print("App UnitTest")
os.system('python test/app_test.py')
time.sleep(1)

print("Finished Test Process")
