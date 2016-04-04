#!/usr/bin/env python
import unittest
# import mysql.connector
from database import run_sql_in_parallel

__date__ = '2015-09-22'


class TestDBConnect(unittest.TestCase):

    def test_get_connection(self):
        cnx = run_sql_in_parallel.get_conn('photoalbums')

        photoalbums_exp = {
            '_user': 'admin',
            '_password': '123photo!',
            '_database': 'photoalbums',
            '_host': '127.0.0.1',
            '_port': 23307,
        }

        for key, value in photoalbums_exp.items():
            self.assertEqual(
                value, cnx.__dict__[key],
                msg="Default for '{0}' did not match.".format(key))

        cnx.close()

if __name__ == '__main__':
    unittest.main()
