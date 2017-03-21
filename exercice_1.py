#!/usr/bin/env python
import urllib2
import json
import pprint

response = urllib2.urlopen('http://beta.ckan.org/api/3/action/package_list')
assert response.code == 200

response_dict = json.loads(response.read())
assert response_dict['success'] is True

result = []

for package in response_dict['result']:
    response = urllib2.urlopen('http://beta.ckan.org/api/3/action/package_show?id=%s'%package)
    assert response.code == 200

    response_dict = json.loads(response.read())
    assert response_dict['success'] is True
    result.append(response_dict['result'])

print pprint.pprint(result)
