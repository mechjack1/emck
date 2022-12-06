import sys

value1 = int(sys.argv[1])

# write your solution here


def recursivesum(x):
    valuet = x
    ones = 0
    total = 0
    while (valuet > 0):
        ones = valuet % 10
        valuet = valuet // 10
        # print(ones, value1)
        # print(valuet)
        # print("+", valuet, ones)
        total = total + ones
        # print(total)
    if total > 9:
        return (recursivesum(total))
    return (total)


print(recursivesum(value1))
