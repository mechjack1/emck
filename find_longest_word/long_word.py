import sys

value1 = sys.argv[1]

# write your solution here
long_list = []

for my_word in value1.split(","):
    if len(long_list) == 0:  # append word if starting
        long_list.append(my_word)
    elif len(long_list) > 0:
        if len(long_list[0]) < len(my_word):  # found larger word, clear list, append
            long_list.clear()
            long_list.append(my_word)
        elif len(long_list[0]) == len(my_word):  # equivalent len on list append
            long_list.append(my_word)

    # print(my_word)
print(','.join(long_list))
