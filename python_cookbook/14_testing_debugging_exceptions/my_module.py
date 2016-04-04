#!/usr/bin/env python

__date__ = '2015-09-22'


def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)
