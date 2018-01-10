import math
#determines if a number is prime based on Wilson's theorem
def isprime(number):
    x1 = math.factorial(number-1) % number #(n-1)! mod n
    if x1+1 == number:
        return 1
    else:
        return 0



    
