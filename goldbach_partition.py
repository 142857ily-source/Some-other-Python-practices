import math

x = math.floor(float(input("Enter a number greater than 5: ")))

def is_prime(n):
    if n < 2: 
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def Goldbach_partition(x):
    while x <= 5:
        print ("Invalid Entry.")
        x = math.floor(float(input("Enter a number greater than 5: ")))
    if x % 2 == 0:
        result = []
        for a in range (2,x):
            b = x - a
            if is_prime(a) and is_prime(b):
                result.append(f"{a}+{b}")
        print (f"{x}={result[0]}")
    if x % 2 ==1 : 
        result = []
        for a in range (2,x):
            for b in range (2, x-a+1):
                c=x-a-b
                if is_prime(a) and is_prime (b) and is_prime(c) and a!=3 and b!=3 and c!=3:
                    result.append(f"{a}+{b}+{c}")
        if result:
            print(f"{x}={result[0]}")
        else:
            print("There is no such partition without at least one of a, b, and c equal to 3.")

Goldbach_partition(x)
