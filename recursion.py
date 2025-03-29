#factorial

def fact(n):
    if(n==1 or n==0):
        return 1
    return n * fact(n-1)

n=int(input("enter number: "))
print(f"factorial is: {fact(n)}")

#sum of n naturnal number

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n


print(f"summation is: {sum(n)}")