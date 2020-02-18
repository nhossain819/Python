"""
Greatest Common Divisor (GCD)
The following function returns the greatest common divisor of two integers.
"""

def gcd(integer1 , integer2):
    max_int = max(integer1 , integer2)
    frame_list = list(range(max_int))
    divisors_int1 = []
    divisors_int2 = []
    for i in frame_list:
        if i == 0:
            continue
        if integer1 % i == 0:
            divisors_int1.append(i)
        if integer2 % i == 0:
            divisors_int2.append(i)
    common_divisors = []
    for i in divisors_int1:
        if i in divisors_int2:
            common_divisors.append(i)
    return max(common_divisors)
