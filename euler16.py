#215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 21000?

print(2**1000)
a = str(2**1000)
sum = 0
for i in a:
    sum += int(i)
print(sum)
