# -*- coding: UTF-8 -*-
import sys

def fizzbuzz(num: int) -> []:
    result = []
    for n in [x for x in range(1,num+1)]:
        if n % 15 == 0:
            result.append('fizz-buzz')
            continue
        if n % 5 == 0:
            result.append('buzz')
            continue
        if n % 3 ==0:
            result.append('fizz')
            continue
        result.append(n)
    return result

try:
    num = int(sys.argv[1])
    if 1 > num:
        exit(-1)
except ValueError:
    exit(-1)

print(fizzbuzz(num))