#!/usr/bin/env python
import unittest
import requests


class TestHello(unittest.TestCase):

    def setUp(self):
        pass

    def test_hello(self):
        print('Testing : test_hello')
        rv = requests.get('http://localhost:5000',auth=('user', 'password'))
        print(rv)
        print(tv.text)
        self.assertEqual('{}'.format(rv), '<Response [200]>')
        self.assertEqual(rv.text, 'Hello World!')

    def test_hello_hello(self):
        print('Testing : test_hello_hello')
        rv = requests.get('http://localhost:5000/hello/',auth=('user', 'password'))
        print(rv)
        print(tv.text)
        self.assertEqual('{}'.format(rv), '<Response [200]>')
        self.assertEqual(rv.text, 'Hello World!')

    def test_hello_name(self):
        print('Testing : test_hello_name')
        name = 'Kazi-Alam'
        rv = requests.get(f'http://localhost:5000/hello/{name}',auth=('user', 'password'))
        print(rv)
        print(tv.text)
        self.assertEqual('{}'.format(rv), '<Response [200]>')
        #self.assertIn(bytearray(f"Hello {name}", 'utf-8'), rv.text)
        self.assertEqual(rv.text, 'Hello Kazi-Alam!\n')


if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()
