import sys

value1 = sys.argv[1]

# write your solution here


def trunc1(myfloat: float, num_dec: int) -> str:
    my_str = str(myfloat)
    dec_pos = my_str.find('.')
    trunc = my_str[:dec_pos+1+num_dec]
    return (trunc)


first_x = value1.find('x')
last_x = value1.find('x', value1.find('x')+1)
equalsign = value1.find('=')
# print('first x', first_x)
# print('last x ', last_x)
# print(value1[:first_x])
# print(value1[first_x+3:last_x])
if value1[:first_x] == '-x':
    a = -1
elif value1[:first_x] == 'x':
    a = 1
else:
    a = int(value1[:first_x])

if value1[first_x+3:last_x] == '-x':
    b = -1
elif value1[first_x+3:last_x] == 'x':
    b = 1
else:
    b = int(value1[first_x+3:last_x])

    c = int(value1[last_x+1:equalsign])

underroot = pow(b, 2) - 4 * a * c
# print(a)
# print(b)
# print(c)
# print('underroot', underroot)
if underroot < 0:
    print('imaginary,imaginary')
else:
    root1 = (-1 * b + pow(underroot, 0.5))/(2*a)
    root2 = (-1 * b - pow(underroot, 0.5))/(2*a)

    print(trunc1(root1, 5)+','+trunc1(root2, 5))
# x = [-b ± √(b2 – 4ac)]/2a
