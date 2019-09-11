import os
import sys
import unittest

import kubernetes.client
from kubernetes import client, config
from kubernetes.client.rest import ApiException

config.load_kube_config()
v1 = client.CoreV1Api()

mylist = ['elasticsearch-master', 'elasticsearch-data', 'filebeat-dashboard', 'filebeat-template', 'filebeat', 'kibana', 'flask-app']
mydict = {'elasticsearch-master': False, 'elasticsearch-data': False, 'filebeat-dashboard':False, 'filebeat-template':False, 'filebeat':False, 'kibana':False, 'flask-app':False}


class TestIntegration(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_kubernetes_pods(self):
        print("----Running Integration test----")
        ret = v1.list_pod_for_all_namespaces(watch=False)
        for i in ret.items:
            if i.metadata.namespace == 'default':
                for j in mylist:
                    if j in i.metadata.name:
                        if i.status.phase == 'Running':
                            mydict[j] = True
                        #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.name, i.status.phase))
        print(mydict)
        overallstatus = True
        for name, state in mydict.items():
            if state == False:
                overallstatus = False
                break
        print("------------------------------------------")
        self.assertEqual(overallstatus, True)



if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()
