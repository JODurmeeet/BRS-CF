from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
n=int(input("enter the no. of term you want to find:"))
if n==1:
    print(1)
elif n==2:
    print(1)
else:
    for i in range(1,n+1):
        output = []
        nth = (i - 1) + (i - 2)
        output.insert(i,nth)
        print(nth)
        
        
    