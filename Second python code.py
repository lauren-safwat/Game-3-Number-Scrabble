print ("Welcome to Number Scrabble Game")
print ("How to play?")
print ("This game is played with a list of numbers between 1 and 9.  Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
A = [1,2,3,4,5,6,7,8,9]
print (A)
P1 = []
P2 = []
p1 = int(input ("Player 1: Pick a number from the list: "))
while (not p1 in A):
    p1 = int(input("Invalid number, Enter another number from the list: "))
P1.append(p1)
A.remove(p1)
print (A)
p2 = int(input ("Player 2: Pick a number from the list: "))
while (not p2 in A):
    p2 = int(input("Invalid number, Enter another number from the list: "))
P2.append(p2)
A.remove(p2)
print (A)
p1 = int(input ("Player 1: Pick a number from the list: "))
while (not p1 in A):
    p1 = int(input("Invalid number, Enter another number from the list: "))
P1.append(p1)
A.remove(p1)
print (A)
p2 = int(input ("Player 2: Pick a number from the list: "))
while (not p2 in A):
    p2 = int(input("Invalid number, Enter another number from the list: "))
P2.append(p2)
A.remove(p2)
print (A)
p1 = int(input ("Player 1: Pick a number from the list: "))
while (not p1 in A):
    p1 = int(input("Invalid number, Enter another number from the list: "))
P1.append(p1)
A.remove(p1)
if (P1[0]+P1[1]+P1[2]==15):
    print ("CONGRATULATIONS *_*, Player 1 Won!!!")
else:
    print (A)
    p2 = int(input ("Player 2: Pick a number from the list: "))
    while (not p2 in A):
        p2 = int(input("Invalid number, Enter another number from the list: "))
    P2.append(p2)
    A.remove(p2)
    if (P2[0]+P2[1]+P2[2]==15):
        print ("CONGRATULATIONS *_*, Player 2 Won!!!")
    else:
        print (A)
        p1 = int(input ("Player 1: Pick a number from the list: "))
        while (not p1 in A):
            p1 = int(input("Invalid number, Enter another number from the list: "))
        P1.append(p1)
        A.remove(p1)
        if (P1[0]+P1[1]+P1[3]==15) or (P1[0]+P1[2]+P1[3]==15):
            print ("CONGRATULATIONS *_*, Player 1 Won!!!")
        else:
            print (A)
            p2 = int(input ("Player 2: Pick a number from the list: "))
            while (not p2 in A):
                p2 = int(input("Invalid number, Enter another number from the list: "))
            P2.append(p2)
            A.remove(p2)
            if (P2[0]+P2[1]+P2[3]==15) or (P2[0]+P2[2]+P2[3]==15):
                print ("CONGRATULATIONS *_*, Player 2 Won!!!")
            else:
                print (A)
                p1 = int(input ("Player 1: Pick a number from the list: "))
                while (not p1 in A):
                    p1 = int(input("Invalid number, Enter another number from the list: "))
                P1.append(p1)
                A.remove(p1)
                if (P1[0]+P1[1]+P1[4]==15) or (P1[0]+P1[2]+P1[4]==15) or (P1[0]+P1[3]+P1[4]==15):
                    print ("CONGRATULATIONS *_*, Player 1 Won!!!")
                else:
                    print ("The game is a draw, Play Again!")
    
