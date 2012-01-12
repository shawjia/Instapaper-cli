#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import sys
from config import instapaper_user, instapaper_pass

class Instapaper(object):
    def __init__(self, username, password):
        self.username = str(username)
        self.password = str(password)
        self.auth_url = 'https://www.instapaper.com/api/authenticate'
        self.add_url  = 'https://www.instapaper.com/api/add'

    def check_login(self):
        r = requests.get(self.auth_url, auth=(self.username, self.password))
        if r.status_code == 200:
            return True
        elif r.status_code == 403:
            print '403: wrong username/password'
        else:
            print '500: internal error'
        return False

    def add(self, url):
        url = self.add_url + '?url=' + url
        r = requests.get(url, auth=(self.username, self.password))
        if r.status_code == 201:
            title = r.headers['X-Instapaper-Title'];
            print "[%s] added!" % title
            return True
        elif r.status_code == 400:
            print '400: bad reques, url needed'
        elif r.status_code == 403:
            print '403: wrong username/password'
        else:
            print '500: internal error'
        return False


def main():
    if len(sys.argv) < 2:
        print 'url needed'
    else:
        url = sys.argv[1]
        ins = Instapaper(instapaper_user, instapaper_pass)
        ins.add(url)

if __name__ == '__main__':
    main()
