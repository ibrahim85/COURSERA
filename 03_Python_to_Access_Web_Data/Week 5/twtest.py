#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     24/11/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib

import twurl

print 'Calling Twitter'

url = twurl.augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
        {'screen_name': 'Trenton_EE', 'count': '2'})

print url
connection = urllib.urlopen(url)
data = connection.read()
print data
headers = connection.info().dict
print headers