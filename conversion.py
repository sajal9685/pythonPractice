#farenheit to celsius
def fa_to_cel(f):
    return 5*(f-32)/9

f=int(input("enter temperature in farenheit: "))

c=fa_to_cel(f)

print(f"tempertaure is : {round(c,2)}")

#inches to cm
def in_to_cm(n):
    return n*2.54

n=int(input("enter the number in inches: "))

cm=in_to_cm(n)

print(f"the cm is : {cm}")