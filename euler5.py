import euler3

def listofprime(num):
    a = []
    for i in range(2, num+1):
        if euler3.is_prime(i):
            a.append(i)
    return a
                
print(listofprime(20))
