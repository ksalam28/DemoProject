import os
import sys
import unittest

import kubernetes.client
from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()
v1 = client.CoreV1Api()

mylist = ['elasticsearch-master', 'elasticsearch-data', 'filebeat-dashboard', 'filebeat-template', 'filebeat', 'kibana', 'flask-app']


class TestInfrastructure(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kubernetes_pods(self):
        print("----Listing pods for DemoProject----")
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            if i.metadata.namespace == 'default':
                for j in mylist:
                    if j in i.metadata.name:
                        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.name, i.status.phase))
        print("------------------------------------------")
        pass

    def test_kubernetes_services(self):
        print("----Listing services for DemoProject----")
        ret = v1.list_service_for_all_namespaces(watch=False)
        for i in ret.items:
            if i.metadata.namespace == 'default':
                for j in mylist:
                    if j in i.metadata.name:
                        print ("-> " + i.metadata.name)
        print("------------------------------------------")
        pass


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()
