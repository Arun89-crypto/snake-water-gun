import random


def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "w":
            return True
        elif you == "s":
            return False

print("Computers turn computer chose : ***")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

you = input("Your turn: Snake(s) Water(w) Gun(g)??? : ")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")


if None:
    print("The game is tied")
elif a:
    print("You won the game  :) :) :)")
else:
    print("You Lose :( :( :(")


