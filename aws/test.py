__author__ = 'bach'

import boto
import time

s3 = boto.connect_s3(profile_name='bach')

bucket = s3.create_bucket('boto-demo-%s' % int(time.time()))

key = bucket.new_key('mykey')
key.set_contents_from_string("Hello, World!")

time.sleep(2)

print(key.get_contents_as_string())
