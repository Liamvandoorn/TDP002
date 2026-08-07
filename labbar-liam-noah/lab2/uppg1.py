#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#ramen

def frame(a):
   print((len(a)+4)*'*','\n* ',a,' *\n',(len(a)+4)*'*', sep="")

frame("Välkommen till python")

#pyramiden

def triangle(rader):
   for i in range(rader): # i är antalet gånger det loopats om... 
      print((1+i)*'*')
      
triangle(4)

print('\n')
#flagga

def flag(n):
   for j in range(2):
      print('\n'*n,end='')
      for i in range(4*n):
         print(n*'*'*10,n*" ",n*'*'*10, sep="")

flag(3)
