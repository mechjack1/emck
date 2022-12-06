import sys

value1 = sys.argv[1]
value2 = sys.argv[2]

# write your solution here
value1 = value1.split(',')
value2 = value2.split(',')
result = len(value2)*2*[0]
for i in range(0, len(value2)):
    result[2*i] = value1[i]
    result[2*i+1] = value2[i]

print(','.join(result))
