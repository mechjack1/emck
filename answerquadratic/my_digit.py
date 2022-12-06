def trunc1(myfloat: float, num_dec: int) -> str:
    my_str = str(myfloat)
    dec_pos = my_str.find('.')
    trunc = my_str[:dec_pos+1+num_dec]
    return (trunc)


print(trunc1(0.957081545064377, 3))
print(trunc1(100.9565368, 4))
