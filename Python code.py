import sys
print ("Welcome to Number Scrabble Game")
print ("How to play?")
print ("This game is played with a list of numbers between 1 and 9.  Each player takes turns picking a number from the list. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15, the game is a draw.")
A=[1,2,3,4,5,6,7,8,9]
P1=[]
P2=[]
counter1=0
counter2=0
End_counter=0
x = False
for i in range(5):
    print ("Player 1 turn")
    print (A)
    p1=int(input("Enter a number from the list: "))
    while (p1 not in A):
        p1=int(input("Invalid number, Enter another number from the list: "))
    P1.append(p1)
    A.remove(p1)
    print ("Your list= ",P1)
    counter1=counter1+1
    End_counter=End_counter+1
    if (counter1 >= 3):
        for x in range (len(P1)):
            for y in range (x+1,len(P1)):
                for z in range (y+1,len(P1)):
                    if (P1[x]+P1[y]+P1[z]==15):
                        print ("CONGRATULATIONS *_*, PLAYER 1 WON!")
                        sys.exit()
                        x=True
    if(End_counter==5):
        print("its a draw")
        sys.exit()
    
    print ("Player 2 turn")
    print (A)
    p2=int(input("Enter a number from the list: "))
    while (p2 not in A):
        p2=int(input("Invalid number, Enter another number from the list: "))
    P2.append(p2)
    A.remove(p2)
    print ("Your list= ",P2)
    counter2 += 1
    if (counter1 >= 3):
        for x in range (len(P2)):
            for y in range (x+1,len(P2)):
                for z in range (y+1,len(P2)):
                    if (P2[x]+P2[y]+P2[z]==15):
                        print ("CONGRATULATIONS *_*, PLAYER 2 WON!")
                        sys.exit()
                        x=True
