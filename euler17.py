# Problem 17
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
import math
def numtostr(num):

    numdic = {
        "1" : "one", "2" : "two", "3" : "three", "4" : "four",
        "5" : "five", "6" : "six", "7" : "seven", "8" : "eight",
        "9" : "nine", "10" : "ten", "11": "eleven", "12": "twelve",
        "13" : "thirteen", "14" : "fourteen", "15" : "fifteen", "16": "sixteen",
        "17" : "seventeen", "18" : "eighteen", "19" : "nineteen", "20" : "twenty",
        "30" : "thirty", "40" : "fourty", "50" : "fifty" , "60" : "sixty",
        "70" : "seventy", "80" : "eighty", "90" : "ninety",
        "100" : "hundred"
    }
    try:
        return numdic["1000"]
    except:

def numsep(num):
    str1 = ""
    str2 = ""
    str3 = ""
    if num >= 100:
        str1 = str(math.floor(num/100)) + "00"
        num = num - int(str1)
    elif num >= 10:
        try:
            str2 = numdic[str(num)]
            str3 = math.floor(int(str1)/100)



