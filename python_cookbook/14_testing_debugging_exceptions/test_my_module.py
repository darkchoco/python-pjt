#!/usr/bin/env python

__date__ = '2015-09-22'


from io import StringIO
from unittest import TestCase
from unittest.mock import patch
import my_module


class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            my_module.urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)

if __name__ == '__main__':
    import unittest
    unittest.main()
