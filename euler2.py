import math

def fib(num):
    if num == 0 or num  == 1:
        return 1
    if num > 1 :
        return fib(num - 1) + fib(num - 2)
        

print(fib(35))
sum = 0
for i in range(35):
    if fib(i) < 4000000 and fib(i) % 2 ==0:
        sum += fib(i)

print(sum)