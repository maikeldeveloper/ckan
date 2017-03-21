#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint


response = urllib2.urlopen('http://beta.ckan.org/api/3/action/resource_search?query=url_type:upload')
assert response.code == 200

response_dict = json.loads(response.read())

assert response_dict['success'] is True

print("Internal resources: %s"%response_dict['result']['count'])
