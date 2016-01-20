#-------------------------------------------------------------------------------
'''
Write a program to read through the mbox-short.txt and figure out the distribution
by hour of the day for each of the messages. You can pull the hour out from the
'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted
by hour as shown below. Note that the autograder does not have support for the
sorted() function.
'''
# Author:      Trenton J. McKinney
# Created:     21/09/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#name = raw_input("Enter file:")
name = 'mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[5]
    email = email[0:2]

    counts[email] = counts.get(email,0) + 1 # same function as the previous 4 lines

#prints key value as per the assignment
for k,v in sorted(counts.items()):
    print k, v

#Creats a temporary list with value first and key second and then sorts based on value
tmp = list()
for k, v in counts.items():
    tmp.append((v, k))

print tmp #unsorted

tmp.sort(reverse=True)
print tmp #sorted max value to min value


print sorted([(v,k) for k,v in counts.items()]) #same as previous 6 lines of code except min to max value