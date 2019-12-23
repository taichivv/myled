#!/usr/bin/env python

import time

a = 0.2
b = a*3

if __name__ == '__main__':
    while 1:
        # u ##########
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(3)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(a)
        #.
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(a)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        
        # n ############
        #.
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(2)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(a)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        #.
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(a)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        #.
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(a)
        # ko ##################
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(2)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        #-
        file=open('/dev/myled0','w')
        file.write('1\n')
        time.sleep(a)
        #
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(b)
        file=open('/dev/myled0','w')
        file.write('0\n')
        time.sleep(2)
