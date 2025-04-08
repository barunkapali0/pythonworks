import getpass
print("Rock,paper and scissor game.")
choices=["rock","paper","scissor"]
a=getpass.getpass("Player 1 choose rock paper or scissor:")
b=input("Player 2 choose rock paper or scissor:")
print(f"Player 1 choose: {a}")
print(f"Player 2 choose: {b}")
if a not in choices or b not in choices:
    print("invalid word.")
else:
    
    if b==a:
         print("its a draw!")       
    elif (a=="paper"and b=="rock")or(a=="rock"and b=="scissor")or(a=="scissor"and b=="rock")or(a=="scissor"and b=="paper"):
        print("Player 1 win!") 
    
    else:
        print("player 2 win!")

    
