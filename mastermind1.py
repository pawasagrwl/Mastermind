#to import
import random, string
#Rules
rules=''' ==== The Mastermind game ====
Objective of the Game:
The computer picks a sequence of 4 colors, each one being one of any of seven colors.
Your task is to guess the exact positions of the colors in the
sequence in as few guesses as possible. You will get 12 chances for guessing.
After each guess, the computer gives you a score of exact and partial matches.
A black peg indicates an exact match, a white peg a partial match (right color, wrong position).

Rules:
    1. The sequence can contain pegs of colors: red, yellow, green, blue, white, purple, orange
    2. A color can be used any number of times in the sequence.
    3. All four pegs of the secret sequence will contain a color - 
       no blanks/empties are allowed.
    4. Each guess must consist of 4 peg colors - no blanks.
    5. Enter \'rules\' for getting rules and \'quit\' to quit the game


You should enter each color of your guess by typing its first letter.
--------------------------------------------------------------------------------------------------

    '''
#to generate a random combination of 4 colors
def combination():
    global code
    code=[]
    for i in range(4):
        code.append(random.choice(["R","G","Y","B","W","P","O"]))
    return code
#asking for input and checking it
def input_check():
    print ('''Guess the secret color combination in the correct order.
\nPossible colors are Red, Yellow, Green, Blue, White, Purple, and Orange
''')
    global guessList, colorletters
    guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
    while True:
        colorletters=["R","Y","G","B","W","P", "O"]
        if len(guess)!=4:
            if guess.lower()=='rules':
                print rules
                guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
            else:
                guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
        else:
            if guess.lower()=='quit':
                z=raw_input('Are you sure you want to quit.\nEnter \'y\' for yes and \'n\' for no\n: ')
                if z.lower()=='y':
                    quit()
                elif z.lower()=='n':
                     guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
                else:
                    print 'Invalid Input'
                    guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
            else:
                guessList=list(guess.upper())
                wrongLetters=False
                for i in guessList:
                    if i not in colorletters:
                        wrongLetters=True
                if wrongLetters==True:
                    print "You can only enter R, Y, G, B, W, P, O"
                    guess=raw_input("Enter your guess as 4 letters e.g. XXXX: ")
                else:
                    return guessList
#the no. of black and white pegs
def blacks_whites(code, guessList):
    blacks=0
    whites=0
    pegsChecked=[]
    temp_code=code[:]
    for i in range(4):
        if guessList[i]==temp_code[i]:
            blacks+=1
            guessList[i]="X"    #in order to cross out the ones already checked
            temp_code[i]="X"
    for j in range(4):
        if guessList[j] in temp_code and guessList[j]!="X" and guessList[j] not in pegsChecked:
            if temp_code.count(guessList[j])>guessList.count(guessList[j]):
                whites+=guessList.count(guessList[j])
            else:
                whites+=temp_code.count(guessList[j])
            pegsChecked.append(guessList[j])
    if blacks>0:
        print "Black pegs: ",blacks       #black pegs for exact match
    if whites>0:
        print "White pegs: ",whites         #white pegs for right color wrong position
    if blacks==0 and whites==0:
        print "Oops, try again, you got nothing right!"
#the result
def result(correct,code):
    if correct:
        print "YAY YOU WON ! ! YOU GOT IT IN",chances,"CHANCES!!!"
    else:
        print "SORRY YOU LOST!"
#the game
def play_game():
    secret_code=combination()
    global chances
    chances=0
    correct=False
    while chances<12:
        guess_code=input_check()
        chances+=1
        correct=guessList==code
        if correct:
            break
        blacks_whites(code,guessList)
    result(correct,code)
#menu
def menu():
    main_menu= """
----------------
-- Mastermind --
----------------
   R)Rules
   P)Play
   Q)Quit
"""
    while True:
        print main_menu
        choice1=raw_input("Choice :")
        choice=choice1.upper()
        if choice=="P":
            play_game()
        elif choice=='R':
            print rules
        elif choice=='Q':
            z=raw_input('Are you sure you want to quit.\nEnter \'y\' for yes and \'n\' for no\n: ')
            if z.lower()=='y':
                quit()
            elif z.lower()=='n':
                continue
            else:
                print 'Invalid Input'
                continue
        else:
            print 'Invalid input'
            continue
menu()
    
    





    

    

