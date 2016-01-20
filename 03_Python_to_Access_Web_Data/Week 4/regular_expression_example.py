#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     20/11/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
#html = urllib.urlopen('http://www.dr-chuck.com').read()

#sample using a regular expression
links = re.findall('href="(http://.*?)"',html)
#print links[10]
for link in links:
       print link


