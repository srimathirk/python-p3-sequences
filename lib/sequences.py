#!/usr/bin/env python3

def print_fibonacci(length):
    num = []
    if length > 0:
        num.append(0)
    if length > 1:
        num.append(1)
    count = 2
    while count < length :
        num.append(num[count - 1] + num[count - 2])
        count += 1
    print(num)
#print_fibonacci(8)
