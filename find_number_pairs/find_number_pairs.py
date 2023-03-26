import sys
import json

start_list =[]
end_list =[]

value1 = sys.argv[1].strip(" ")

value1 = value1.replace("[","")
value1 = value1.replace("]","")
value1=list(map(int, value1.split(",")))

start_list = value1[0:-1]
sum_num = value1[-1]

print("startlist",start_list)
print("sum_num",sum_num)
for i in start_list:
    if (sum_num-i)in start_list and not((sum_num-i, i) in end_list) and not(sum_num-i == i):
        end_list.append((i, sum_num-i))

print(end_list)