#-------------------------------------------------------------------------------
# Name:        module1
'''
Write a program to read through the mbox-short.txt and figure out who has the
sent the greatest number of mail messages. The program looks for 'From ' lines
and takes the second word of those lines as the person who sent the mail. The
program creates a Python dictionary that maps the sender's mail address to a
count of the number of times they appear in the file. After the dictionary is
produced, the program reads through the dictionary using a maximum loop to find
the most prolific committer.
'''
#
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


#name = raw_input("Enter file:")
name = 'mbox-short.txt'
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

counts = dict()



for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]



    '''
    if email not in counts:  ##if key doesn't exist, adds it with a value of 1
        counts[email] = 1
    else:                    ##else increases the value by 1
        counts[email] += 1
    '''
    counts[email] = counts.get(email,0) + 1 # same function as the previous 4 lines


#print counts

largest = None
address = None

for key in counts:
    #print key, counts[key]
    if largest is None or counts[key] > largest:
        largest = counts[key]
        address = key

print address, largest


#books['treeses'] = books.get('treeses',0) + 1 ##if the key doesn't exist, it's added with a value of 1
#books['treeses'] = books.get('treeses',-1) + 1 ##if the key doesn't exist, its' added with a value of 0









