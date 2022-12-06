import sys

value1 = sys.argv[1]

# write your solution here
my_list = value1.split(',')
my_start = my_list[1].find(my_list[0])
my_end = my_list[1].find(my_list[0]) + len(my_list[0]) - 1
print(my_start + my_end)
