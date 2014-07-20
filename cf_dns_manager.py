#!/usr/bin/env python
#
# Similar to cf_update_dns but in python

import json
import requests
import sys
from datetime import datetime

CF_TOKEN = ''
CF_EMAIL = ''
CF_DZONE = ''


class CloudFlare(object):

    API_URL = 'https://www.cloudflare.com/api_json.html'

    def __init__(self, api_key, cf_email):
        self.tkn = api_key
        self.email = cf_email








