import sys
import json

start_list =[]
int_list = '0123456789'
value1 = sys.argv[1].strip(" ")
print(type(value1))
value1 = value1.split("]")
value1[0] = value1[0]+"]"


value1[1] = int(value1[1].strip(','))
for eachitem in value1[0]:
    if eachitem in int_list:
        start_list.append(int(eachitem))

print(start_list, value1[1])

