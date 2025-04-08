print("voting process for the parties.The parties are:")
print("Here are 5 members so each member have to do the voting.")
print("1.Congress\n2.yemale\n3.raprapa\n4.maubadi\n5.swotantra")
a=int(input("Voter number 1 choose the number shown above to vote:"))
if a==1:
    print("voting done to kangress")
elif a==2:
    print("voting done to yemale")
elif a==3:
    print("voting done to raprapa")
elif a==4:
    print("voting done to maubadi")
elif a==5:
    print("voting done to swotantra party")    
else:
    print("invalid number choosen\n")

b=int(input("Voter number 2 choose the number shown above to vote:"))
if b==1:
    print("voting done to kangress")
elif b==2:
    print("voting done to yemale")
elif b==3:
    print("voting done to raprapa")
elif b==4:
    print("voting done to maubadi")
elif b==5:
    print("voting done to swotantra party")     
else:
    print("invalid number choosen\n")

c=int(input("Voter number 3 choose the number shown above to vote:"))
if c==1:
    print("voting done to kangress")
elif c==2:
    print("voting done to yemale")
elif c==3:
    print("voting done to raprapa")
elif c==4:
    print("voting done to maubadi")
elif c==5:
    print("voting done to swotantra party")     
else:
    print("invalid number choosen\n")   

d=int(input("Voter number 4 choose the number shown above to vote:"))
if d==1:
    print("voting done to kangress")
elif d==2:
    print("voting done to yemale")
elif d==3:
    print("voting done to raprapa")
elif d==4:
    print("voting done to maubadi")
elif d==5:
    print("voting done to swotantra party")     
else:
    print("invalid number choosen\n")

e=int(input("Voter number 5 choose the number shown above to vote:"))
if e==1:
    print("voting done to kangress")
elif e==2:
    print("voting done to yemale")
elif e==3:
    print("voting done to raprapa")
elif e==4:
    print("voting done to maubadi")
elif e==5:
    print("voting done to swotantra party")     
else:
    print("invalid number choosen\n")

vote=[a,b,c,d,e]
counta=0
countb=0
countc=0
countd=0
counte=0
for i in vote:
    if i==1:
        counta=counta+1
    elif i==2:
        countb=countb+1
    elif i==3:
        countc=countc+1
    elif i==4:
        countd=countd+1
    elif i==5:
        counte=counte+1
    else:
        print("invalid")  
print("\nVoting Results:")
print(f"Kangress: {counta}")
print(f"Yemale: {countb}")
print(f"Raprapa: {countc}")
print(f"Maubadi: {countd}")     
print(f"Swotantra party: {counte}")         
    


    
    
    
