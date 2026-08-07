#! /usr/bin/env python3
# -*- coding: utf-8 -*-

result = 0 
for i in range(513):
    result += i
print(result)

result = 1 
for i in range(1,513):
    result = i * result
print(result)
