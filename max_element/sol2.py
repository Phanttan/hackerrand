#!/bin/python3
"""
https://www.hackerrank.com/challenges/maximum-element
"""
#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    stack = []
    sorted_stack = []
    answer = []
    for i in range(len(operations)):
        query = list(map(int, operations[i].split()))
        if query[0] == 1:
            stack.append(query[1])
            sorted_stack.append(query[1])
            sorted_stack.sort()
        elif query[0] == 2:
            sorted_stack.remove(stack.pop())
        else:
            answer.append(sorted_stack[-1])
    return answer


if __name__ == '__main__':

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)
    print(res)

