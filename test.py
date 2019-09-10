import os
import time
import threading


def thread1():
    print("port-forwarding for service/flask-app 5000")
    os.system('kubectl port-forward service/flask-app 5000')


def thread2():
    print("App Funtional test starting...")
    os.system('python test/app_test.py')


if __name__ == "__main__":
    threads = []
    print("Starting Test Process")
    os.system('pip install -r test-requirements.txt')
    time.sleep(1)
    print("Kubernetes Infrastructure Test")
    os.system('python test/kubernetes_test.py')
    time.sleep(1)
    t1 = threading.Thread(name="port-forwarding", target=thread1)
    t1.start()
    time.sleep(3)
    threads.append(t1)
    t2 = threading.Thread(name="flask-app-test", target=thread2)
    threads.append(t2)
    t2.start()

    while True:
        time.sleep(1)
        if not t2.isAlive():
            for thread in threads:
                thread.join()
            break

    time.sleep(1)
    print("Kubernetes Integration Test")
    os.system('python test/integration_test.py')

    print("Finished Test Process")
