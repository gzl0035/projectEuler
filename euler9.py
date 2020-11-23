#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.


print(200*375*425)
for c in range(500,1,-1):
    for a in range(1,500):
        b = 1000 - c - a
        if a*a + b*b == c*c:
            print("a is " + str(a) + " b is " + str(b) + " c is " + str(c))
