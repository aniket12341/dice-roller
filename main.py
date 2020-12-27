import random
print("---Welcome to Aniket's Ludo---")
input("Enter a key to roll the dice")
while True:
    lol = random.randint(1, 6)
    print("", lol)
    b = input("Enter a key to roll again")
    if (b=='q'):
        break