# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math
def is_factor(num,div):
    if num/div == math.ceil(num/div):
        return True
    else:
        return False

def is_prime(num):
    for i in range(2,int(math.floor(math.sqrt(num)))+1):
        if num/i == math.ceil(num/i):
            return False
    return True

def biggest_print(a):
    for i in range(1,int(math.ceil(math.sqrt(a)))):
        if is_factor(a,i):
            print(i)
            print(is_prime(i))
            if is_prime(int(a/i)):
                return int(a/i)

print(is_prime(9))