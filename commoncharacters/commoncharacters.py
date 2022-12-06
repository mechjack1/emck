import sys

value1 = sys.argv[1]
value1 = value1.replace(' ', '')
my_dict = {}
final_dict = {}
longest = 0
out_string = ''

for each_char in value1:

    if each_char in my_dict.keys():
        my_dict[each_char] += 1
    else:
        my_dict[each_char] = 1

for each_char in my_dict.keys():

    if my_dict[each_char] > longest:
        final_dict = {}
        final_dict[each_char] = my_dict[each_char]
        longest = my_dict[each_char]
    elif my_dict[each_char] == longest:
        final_dict[each_char] = my_dict[each_char]


print(", ".join(final_dict.keys()))
