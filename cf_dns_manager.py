#!/usr/bin/env python
#
# CloudFlare DNS Manager

import json
import requests
import sys
import quote
from datetime import datetime
from urllib2 import urlopen

CF_TOKEN = ''
CF_EMAIL = ''
CF_DZONE = ''


class CloudFlare(object):

    API_URL = 'https://www.cloudflare.com/api_json.html'

    def __init__(self, api_key, cf_email):
        self.tkn = api_key
        self.email = cf_email

    def rec_load_all(self, cf_zone):
        """
        Lists all DNS records for given domain
        :param cf_zone: Domain for which we need to fetch records
        :return: dict
        """

        return self.__main__({'a':'rec_load_all', 'z':cf_zone})['recs']

    def __main__(self, cf_auth):

        cf_auth['tkn'] = self.tkn
        cf_auth['email'] = self.email

        output = []

        for key, value in cf_auth.iteritems():
            if value:
                output.append('%s=%s' % (quote(key), quote(str(value))))
        cf_auth = '&'.join(output)

        response = json.loads(urlopen(self.API_URL, cf_auth).read())
        if response['result'] == 'success':
            return response.get('response', True)
        else:
            raise EnvironmentError('Invalid response received from API\r\n%s' % response)


if __name__ == '__main__':
    print test