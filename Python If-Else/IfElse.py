#!/bin/python3

N=int(input())
if N%2!=0:
    print("Weird")
elif N in range(2,6):
    if N%2 ==0:
        print("Not Weird")
elif N in range(6,21):
    if N%2==0:
        print("Weird")
elif N>20 :
    if N%2==0:
        print("Not Weird")
