#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     09/11/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket

def main():
    pass

def my_socket_test():

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.pythonlearn.com', 80))

    mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

    while True:
        data = mysock.recv(512)
        if ( len(data) < 1) :
            break
        print data
    mysock.close()

def my_socket_test2():

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('www.py4inf.com', 80))

    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')

    while True:
        data = mysock.recv(512)
        if ( len(data) < 1) :
            break
        print data
    mysock.close()

if __name__ == '__main__':
    main()

    my_socket_test()