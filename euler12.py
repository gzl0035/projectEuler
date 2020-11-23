import math
import numpy
import matplotlib.pyplot as plt
def trigen(num):
    return int(num * (num + 1)/2)

def numdiv(num):
    count = 0
    for i in range(1,num+1):
        if num / i == math.floor(num /i):
            count += 1
    return count

x = numpy.zeros((2,1000))
for i in range(1,1000):
    x[1,i-1] = int(trigen(i))
    x[0,i-1] = int(numdiv(trigen(i)))


plt.plot(x[1],x[0])

plt.show()
