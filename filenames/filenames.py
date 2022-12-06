import sys

value1 = sys.argv[1]
file_list_new = []
file_list = value1.split(', ')

for eachitem in file_list:
    if eachitem in file_list_new:
        for i in range(1, 1000):
            new_file_name = eachitem + '(' + str(i) + ')'
            if new_file_name not in file_list_new:
                file_list_new.append(new_file_name)
                break
    else:
        file_list_new.append(eachitem)

print(', '.join(file_list_new))
