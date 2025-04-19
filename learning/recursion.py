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

#sum of n odd numbers

def sumOdd(n):
    if n<=0:
        return 0
    else:
        return (2*n-1) + sumOdd(n-1)
     

print(f"summation is: {sumOdd(n)}") 