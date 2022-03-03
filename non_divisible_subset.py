#!/bin/python3

import math
import os
import random
import re
import sys
import Fraudulent_Activity_var
# python3 C:\Documents\Technology\Python\hackerrank\non_divisible_subset.py

output = []
debug_flag = True
#debug_flag = False
def debug(stmt):
    if debug_flag == True:
        print(stmt)

def nonDivisibleSubset(k, s):
    len_s = len(s)
    s_two = s[:]
    for i in range(0, len_s):
        s_two[i] = s[i]%k
    debug (s)
    debug (s_two)
    s_distinct = list(set(s_two))
    debug (s_distinct)
    count = 0
    out_good_i_j = []
    out_bad_i_j = []
    out_i = []
    out_j = []
    for i in range(1, k):
        if s_two.count(i) > 0:
            for j in range(1, k):
                if s_two.count(j) > 1:
                    if (i+j) % k != 0:
                        debug ('i='+str(i)+' j='+str(j))
                        out_i.append(i)
                        out_good_i_j.append([i, j])
                    else:
                        if i <= j :
                            out_bad_i_j.append([i, j])
    print ( 'out_i')
    print ( out_i)
    distinct_out_i = list(set(out_i))
    print ( 'distinct_out_i')
    print ( distinct_out_i)
    print ( 'out_good_i_j')
    for i in out_good_i_j:
        print ( str(i[0])+' '+str(i[1]))
    print ( 'out_bad_i_j')
    for i in out_bad_i_j:
        print ( str(i[0])+' '+str(i[1]))
    print ( out_bad_i_j)
    out_good_remove_bad_i_j = out_good_i_j[:]
    return 0

#    for i in range(0, len_s-1):
#        for j in range(i+1, len_s):
#            if (s[i]+s[j]) % k != 0:
#                debug ('s[i]='+str(s[i])+' s[j]='+str(s[j]))


#k = 7
#s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

#k = 4
#s = [19, 10, 12, 10, 24, 25, 22]

#k = 4
#s = [19, 10, 12, 10, 24, 25, 22]

#n = 5 
#k = 3
#r_q = 4 
#c_q = 3
#obstacles = [[5, 5],[4, 2],[2, 3]]

#k = 4
#s = [19, 10, 12, 10, 24, 25, 22]

#k = 1000
#s = [19, 10, 12, 10, 24, 25, 22]

k = 7
s = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]

result = nonDivisibleSubset(k, s)
print (result)
