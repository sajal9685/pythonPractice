import random;
comp =random.choice(["s","g","w"])
user=(input("s for snake, g for gun and w for water: "))

if ((user=="s") or (user=="g") or (user=="w")):
    print(f"you choose: {user}")
    print (f"computer choose: {comp}")
    if((user=="s") and (comp=="w")):
        print("you won , congrats")
    elif((user=="s") and (comp=="g")):
        print("you lost , better luck! next time")    
    elif((user=="g") and (comp=="s")):
        print("you won , congrats")    
    elif((user=="w") and (comp=="s")):
        print("you lost , better luck! next time")        
    elif((user=="w") and (comp=="g")):
        print("you won , congrats")   
    elif((user=="g") and (comp=="w")):
        print("you lost , better luck! next time")
    elif((user==comp)):
        print("game tie , try again...")
    else:
        print("game over")
else:
    print("you entered wrong input, try again...")        