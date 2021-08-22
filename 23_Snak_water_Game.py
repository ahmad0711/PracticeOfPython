import random

def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNO = random.randint(1, 3)
if randNO == 1:
    computer = 's'
elif randNO == 2:
    computer = 'w'
elif randNO == 3:
    computer = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(computer, you)

print(f"Computer chose{computer}")
print(f"You chose{you}")

if a == None:
    print("The Game is a tie! ")
elif a:
    print("You Win! ") 
else:
    print("You Loss")