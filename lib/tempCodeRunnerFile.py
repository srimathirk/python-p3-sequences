#!/usr/bin/env python3

#def print_fibonacci(length):
    #num[0] = 0
    #num[1] = 1
    #count = 0
    #while count < length :
        #print(num[0])

        #num[2] = num[0] + num[1]
        #num[0] = num[1]
        #num[1] = num[2]
        #count += 1
#print(num)
#print_fibonacci(8)

def print_fibonacci(length):
    fib_sequence = []
    if length > 0:
        fib_sequence.append(0)
    if length > 1:
        fib_sequence.append(1)
    count = 2
    while count < length:
        fib_sequence.append(fib_sequence[count - 1] + fib_sequence[count - 2])
        count += 1
    for num in fib_sequence:
        print(num)

print_fibonacci(8)
