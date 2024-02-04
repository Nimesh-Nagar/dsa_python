# log(n!) = log(1*2*3...*n) = log(1) + log(2) + .... + log(n)
# floor(log(n!) + 1) gives output as number of digits in n! value
# eg 4! = 24 --> number of digits in 24 is 2 
# eg 8! = 40320 --> number of digits 40320 is 5 

import math

def count_digit(num):
    count = 0

    for i in range(1, num+1):
        count += math.log10(i)

    return math.floor(count) + 1 


print(count_digit(8))
