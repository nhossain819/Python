"""
Least Common Multiple (LCM)
The following function returns the least common multiple (LCM) of two integers.
"""
def lcm(integer1 , integer2):
    max_multiple = integer1 * integer2
    frame_list = list(range(max_multiple))
    multiples_int1 = []
    multiples_int2 = []
    for i in frame_list:
        if i == 0:
            continue
        else:
            multiples_int1.append(i * integer1)
            multiples_int2.append(i * integer2)
    common_multiples = []
    for i in multiples_int1:
        if i in multiples_int2:
            common_multiples.append(i)
    return min(common_multiples)
