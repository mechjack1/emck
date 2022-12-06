import sys

value1 = sys.argv[1]
'''
'''
size = int(value1.lower().split('x')[0])
#print(type(size), size)

end = size * size

total = end
for i in range(1, 4):
    total = total + (end - i * (size-1))
    # print(i, total, end - i*(size - 1))
print(total)
