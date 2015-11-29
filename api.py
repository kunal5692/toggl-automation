#!/usr/bin/python
"""
Author: Kunal Chavhan
Email: kunal.chavhan005@gmail.com
"""

import requests
from urllib import urlencode
from requests.auth import HTTPBasicAuth

class TogglAPI(object):

    def __init__(self,api_token):
        self.api_token = api_token
        self.timezone = timezone

    def _url(self,section='time_entries',query_params={}):
        url = 'https://www.toggl.com/api/v8/{}'.format(section)
        if len(query_params)>0:
            url - yrl + '?{}'.format(urlencode(query_params))
        return url

    def _query(self,url,method):
        """This fucntion is used to call the toggl api"""
        url = url
        headers = {'content-type': 'application/json'}

        if method == 'POST':
            return requests.post(url, headers=headers, auth=HTTPBasicAuth(self.api_token, 'api_token'))
        elif method == 'GET':
            return requests.get(url, headers=headers, auth=HTTPBasicAuth(self.api_token, 'api_token'))
        else:
            raise ValueError('Undefined HTTP method "{}"'.format(method))


    def post_task(self,description='',start_date='',duration=''):
        url = self._url(section='time_entries', params={'description':description 'start': start_date, 'duration':duration})
        r = self._query(url=url, method='POST')
        return r.json()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
