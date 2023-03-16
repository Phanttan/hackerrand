#!/bin/python3
"""
https://www.hackerrank.com/challenges/maximum-element
created by : phanttan
"""

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    """
    Idea : Processing follow the purpose of key 
    """
    _stack = []
    _out = []
    for row in operations:
        row = list(row.split(" "))
        key = int(row[0])
        if key == 1: 
            _stack.append(int(row[1]))
        elif (key == 2) and _stack:
            _stack.pop(-1)
        elif key == 3: _out.append(max(_stack))
    return _out

if __name__ == '__main__':

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)


