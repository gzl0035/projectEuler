# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import euler3
def thprime(i):
    a = 1
    while i != 0:
        a += 1
        if euler3.is_prime(a):
            i -= 1
    return a


print(thprime(10001))

