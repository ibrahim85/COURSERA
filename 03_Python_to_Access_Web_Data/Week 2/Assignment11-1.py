#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     30/10/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


import re

hw = open('regex_sum_169996.txt')

z = []

for line in hw:
    #line = line.rstrip()
    y = re.findall('[0-9]+',line)
    if len(y) > 0:
        z = z + map(int,y)


print z
print len(z)
print sum(z)