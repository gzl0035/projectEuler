#The following iterative sequence is defined for the set of positive integers:

#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

def listofseq(num):
    listofs = [num]
    while num != 1:
        if num % 2 == 0:
            num = num/2
            listofs.append(int(num))
        else:
            num = 3*num + 1
            listofs.append(int(num))
    return listofs

def maxlist(maxnum):
    maxlen = 0
    maxindex = 0
    for i in range(1,maxnum):
        curlen = len(listofseq(i))
        if curlen > maxlen:
            maxlen = curlen
            maxindex = i
    print(listofseq(maxindex))
    print(len(listofseq(maxindex)))
    return maxindex

print(maxlist(1000000))