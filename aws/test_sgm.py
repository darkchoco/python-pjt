#!/usr/bin/env python
import unittest

from aws.sgm import SecurityGroupMgr

__date__ = '2015-10-06'


class TestSecurityGroup(unittest.TestCase):
    def setUp(self):
        # self.param = "83.145.221.209/32"
        self._param = "0.0.0.0/0"
        self._region = "eu-west-1"
        self._profile = "bach"

    def test_connect(self):
        sgm = SecurityGroupMgr(self._param, self._profile, self._region)

        self.assertIsNotNone(sgm.conn)
        self.assertNotEqual(len(sgm.conn.get_all_security_groups()), 0)

        sgm1 = SecurityGroupMgr(self._param, self._profile)
        self.assertIsNotNone(sgm1.conn)
        self.assertNotEqual(len(sgm1.conn.get_all_security_groups()), 0)

    def test_show_sg_ec2_for_ip(self):
        sgm = SecurityGroupMgr(self._param, self._profile, self._region)

        sgm.show_sg_ec2_for_ip()

if __name__ == '__main__':
    unittest.main()
