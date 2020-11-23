#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
import euler3
def is_palindrome(num):
    numstr = str(num)
    numlist = list(numstr)
    #reverlist = numlist.reverse()
    for i in range(len(numlist)):
        if numlist[i] != numlist[-i-1]:
            return False
    return True
max =0
for i in range(999,1,-1):
    for j in range(999,1,-1):
        if i*j > max and is_palindrome(i*j):
            max = i*j



print(max)
