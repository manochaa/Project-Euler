#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      What is the largest prime factor of the number 600851475143 ?
#               i.e. find the larger prime factor of 600851475143
#
# Author:      Ayush Manocha
#
# Created:     30/03/2012
# Copyright:   (c) cain297 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

def is_prime(x):
    i = 2
    while i < x**.5:
        if x%i == 0:
            return False
        i += 1
    return True

num = 600851475143
divisors = []
i = 1

while i < int(num**.5):
    if num%i == 0:
        divisors.append(i)
        i += 1
    i += 1

primeDivisors = []

for i in divisors:
    if is_prime(i) == True:
        primeDivisors.append(i)

print primeDivisors