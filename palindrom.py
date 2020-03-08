# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 05:25:41 2020

@author: user
"""

num=int(input('Enter the number'))
print(num)
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print('entered number is a palindrom number')
else:
    print('Entered number is not a palindrom')