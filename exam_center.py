import sys
import os
''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here
import re 
def find_num(x):
    st = str(x)
    ret = re.search("(2|14)", st)
    if ret is not None:
        return True
    else:
        return False

n = int(input())
curr = 1
act = 1
while curr <= n:
    c = find_num(act)
    if not c:
        curr += 1
    act += 1
print(act-1)