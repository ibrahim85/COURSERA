#-------------------------------------------------------------------------------
# Name:        module1
'''
8.5 Open the file mbox-short.txt and read it line by line. When you find a line
that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the
line (i.e. the entire address of the person who sent the message). Then print
out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
'''


# Author:      Trenton J. McKinney
#
# Created:     20/09/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


#fname = raw_input("Enter file name: ")
fname = 'mbox-short.txt'

if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    print email
    count =  count + 1


print "There were", count, "lines in the file with From as the first word"