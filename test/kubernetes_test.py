import os
import sys
import unittest

import kubernetes.client
from kubernetes import client, config
from kubernetes.client.rest import ApiException
from kubernetes.client.apis.logs_api import LogsApi



class TestKubernetes(unittest.TestCase):
    """ LogsApi unit test stubs """

    def setUp(self):
        self.api = kubernetes.client.apis.logs_api.LogsApi()

    def tearDown(self):
        pass

    def test_kubernetes(self):
        """
        Test case for log_file_list_handler
        """
	config.load_kube_config()
	v1 = client.CoreV1Api()

	print("Listing pods with their IPs:")
	ret = v1.list_pod_for_all_namespaces(watch=False)
	for i in ret.items:
		print("%s\t%s\t%s" %
			  (i.status.pod_ip, i.metadata.namespace, i.metadata.name))	  
        pass


if __name__ == '__main__':
    unittest.main()
