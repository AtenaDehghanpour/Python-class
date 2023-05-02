import random

print("sang...")
print("kaghaz...")
print("gheychi..,")
print()

player1=input("lotfan harekat khod ra vared konid..").lower()

randomnumber=random.randint(1,3)
if randomnumber == 1:
    player2 = "sang"
elif randomnumber == 2:
    player2 = "kaghaz"
elif randomnumber == 3:
    player2 = "gheychi"

print(player2)

if player1==player2:
    print("mosavi!")
elif player1 == "sang" and player2 == "kaghaz":
    print("player2 win")
elif player1 == "sang" and player2 == "gheychi":
    print("player1 win")
elif player1 == "gheychi" and player2 == "kaghaz":
    print("player1 win")
elif player1 == "gheychi" and player2 == "sang":
    print("player2 win")
elif player1 == "kaghaz" and player2 == "sang":
    print("player1 win")
elif player1 == "kaghaz" and player2 == "gheychi":
    print("player2 win")
else:
    print("error!")
