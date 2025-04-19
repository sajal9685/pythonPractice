#multiplication

a=int(input("enter first number: "))
b=int(input("enter second number: "))
def mul(a,b):
    return a*b

mult=mul(a,b)
print(f"multiplication is: {mult}")

#addtition

def sum(a,b):
    return a+b

summ=sum(a,b)
print(f"addition is: {summ}")

#subtraction

def sub(a,b):
    return a-b

subt=sub(a,b)
print(f"subtraction is: {subt}")

#division

def div(a,b):
    return a/b

divi=div(a,b)
print(f"division is: {round(divi,2)}")