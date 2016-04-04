#!/usr/bin/env python

__date__ = '2015-09-22'

import mysql.connector


def get_conn(env):
    photoalbums_db_info = {
        'host': '127.0.0.1',
        'port': 23307,
        'user': 'admin',
        'password': '123photo!',
        'database': 'photoalbums',
    }

    if env == 'photoalbums':
        cnx = mysql.connector.connect(**photoalbums_db_info)
    elif env == 'kick_prd':
        None
    else:
        print('Check argument')
        return None

    return cnx


def close_conn(cnx):
    cnx.close()


