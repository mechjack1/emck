import sys

value1 = int(sys.argv[1])
total = 0

while (value1 > 0):
    ones = value1 % 10
    value1 = value1 // 10
    # print(ones, value1)
    total = total + ones

if total % 2 == 0:
    print("even")
else:
    print("odd")
