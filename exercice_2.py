#!/usr/bin/env python
import urllib2
import json

response = urllib2.urlopen('http://beta.ckan.org/api/3/action/package_search')

assert response.code == 200

response_dict = json.loads(response.read())

assert response_dict['success'] is True

print 'Number of datasets in http://beta.ckan.org: %d'%response_dict['result']['count']
