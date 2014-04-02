# CracklePop v0
# program prints out the numbers 1 to 100(inclusive).
# if the number is divisible by 3, print Crackle instead of the number.
# if the number is divisible by 5, print Pop.
# if it's divisible by both 3 and 5, print CracklePop

import os, sys, math

for i in range(1, 31):                     # list numbers within 1 through 101
    if i % 3 == 0:                         # if the number is divisible by 3
       print 'Crackle',                    # print Crackle
    sys.stdout.softspace=0                 # removes space when printing both
    if i % 5 == 0:                             # if the number is divisible by 5
       print 'Pop'                         # print Pop
    else:              
       print i                             # prints out list of numbers 1 to 100
