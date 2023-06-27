import random
def game(comp,user):
    if(comp==user):
        return None
        #   1st possibility
    elif(comp=='s'):
        if(user=='w'):
            return False
        elif(user=='g'):
            return True
        # 2nd possibility
        elif(comp=='w'):
            if(user=='g'):
                return False
        elif(user=='s'):
            return True
        #   3rd possibility
        elif(comp=='g'):
            if(user=='s'):
                return False
        elif(user=='w'):
            return True
print("Computer turn:Snake(s),Water(w),Gun(g)?")
rand_no=random.randint(1,3)
if(rand_no==1):
    comp='s'
elif(rand_no==2):
    comp='w'
elif(rand_no==3):
    comp='g'  
#  User input  choice                
print("User's turn: Snake(s),Water(w),Gun(g )?")
user=(input("Choose!"))
print(f"Computer chose{comp}")
print(f"User chose{user}")
dec=game(comp,user)
if(dec==None):
    print("Game Tied Hardluck!!")
elif dec:
    print("You Win;-)")
else:
    print("You Lose NT:)")    