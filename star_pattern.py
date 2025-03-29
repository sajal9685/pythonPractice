print(" pattern 1")

n=int(input("enter number: "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="")
    print(" ")

print(" pattern 2")

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"* n, end="")
    else :
        print("*", end="")
        print(" "* (n-2),end="")
        print("*",end="")
    print("") 
   
# n=int(input("enter"))
# for i in range(n):
#     print(" "*n,"*"*i)
#     i+=1

