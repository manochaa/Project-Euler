#-------------------------------------------------------------------------------
# Name:        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Purpose:      232792559
#
# Author:      cain297
#
# Created:     06/04/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

for i in range(2,300000000):
    count = 0
    for j in range(11,21):
        if i%j == 0:
            count += 1

    if count == 10:
        print i
        break