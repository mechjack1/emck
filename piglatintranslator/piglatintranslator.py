import sys

value1 = sys.argv[1]
value1 = value1.split(' ')
final_text = []

for eachitem in value1:
    # print(eachitem[-3:])
    if eachitem[-3:] == 'yay':
        final_text.append(eachitem[: -3])
    else:
        dash_start = eachitem.find('-')

        final_text.append(eachitem[dash_start + 1: -2] + eachitem[:dash_start])


print(' '.join(final_text))
