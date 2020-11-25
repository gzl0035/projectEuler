import math
import numpy
import matplotlib.pyplot as plt

def trigen(num):
    return int(num * (num + 1)/2)

def isint(num):
    if num == math.floor(num):
        return True
    else:
        return False

def numdiv(num):
    count = 0
    middlenum = math.sqrt(num)
    for i in range(1,math.floor(middlenum)+1):
        if isint(num / i):
            count += 1
    if isint(middlenum):
        return count * 2 - 1
    else:
        return count * 2

# for i in range(1,1000000):
#     if numdiv(trigen(i)) >= 500:
#         print(trigen(i))
#         break
print(numdiv(76576500))
# x = numpy.zeros((2,100000))
# for i in range(1,100000):
#     x[1,i-1] = int(trigen(i))
#     x[0,i-1] = int(numdiv(trigen(i)))
# plt.plot(x[1],x[0])

# plt.show()
