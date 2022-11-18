# Imports
# please install openpyxl with the command -> pip install openpyxl

from openpyxl import load_workbook


import random


# Hangman Skeleton


hangmanSkeleton = [r'''
 +--------+                
 |                 
 |       
 |                   
 |
 |=============                  
''', r'''
 +--------+                
 |        0         
 |       
 |                   
 |
 |=============                  
''' ,r'''
 +--------+                
 |        0         
 |       /
 |                   
 |
 |=============                  
''', r'''
 +--------+                
 |        0         
 |       /|
 |                     
 |
 |=============                  
''' , r'''
 +--------+                
 |        0         
 |       /|\
 |                   
 |
 |=============                  
''' , r'''
 +--------+                
 |        0         
 |       /|\
 |       /              
 |
 |=============                  
''' , r'''
 +--------+                
 |        0         
 |       /|\
 |       / \             
 |
 |============                  
''',]


# Initialization and declarations

letterGuessed = " "

hangManint = 0

# functions

def failure():
    print("You have lost the game")


def diffLevel (diffvalue):
    diffLevel = diffvalue
    capdiffLevel1 = diffLevel.upper()
    return capdiffLevel1

def gameStart():
    print()
    print("WELCOME TO HANGMAN GAME")
    print("NOTE*")
    print("You will be provided hints accross the game!")
    print("The higher difficulty level will give you less no of chances!")

    print()
    # choosing the difficulty level
    print("Choose the level of difficulty (L, M, H): " , end='')
    userInput = input()
    capdiffLevel = diffLevel(userInput)

    # sets the difficulty level for the user

    while (capdiffLevel!= "L" or capdiffLevel!="M" or capdiffLevel!="H"):
        
        if (capdiffLevel== "L"):
            return 7
            break
        elif (capdiffLevel== "M"):
            return 5
            break
        elif (capdiffLevel== "H"):
            return 3
            break
        else:
            print("Enter the correct input from the option")
            print("Choose the level of difficulty (L, M, H): ", end='')
            insidelevel = input()
            print()
            capdiffLevel = diffLevel(insidelevel)
        
      # Game begins
    
    print()
    print(f"Word Hint:{hintRealWord}")
    print()
    
    # for x in realWord:
    #     print("_ ", end='')
    # print()



# randomly getting the name and desc from the file
randomindex = random.randint(1, 9)

gameWords = load_workbook('guesswords.xlsx')
sheetName = gameWords.active
rows  =sheetName.rows
fileHeaders = [cell.value for cell in next(rows)]

#guess word picked randomly form the file

excelData  = {}
dummyList = []

for row in rows:
    
    for title, cell in zip(fileHeaders, row):
        excelData[title] = cell.value

    dummyList.append(excelData)



# I will randomly choose this word from a excel sheet for final drat
realWord = str(dummyList[randomindex]['guessWord'])
hintRealWord = str(dummyList[randomindex]['guessHint'])

guessNo = 0


# prints out the initial part of the game

  
guessNo = gameStart()
hangManint= guessNo

for alphabets in realWord:
    if guessNo>0:
        if  alphabets not in letterGuessed.upper() :
            print("_ ", end='')
print()
  
while (guessNo>0):
   
    
    # Taking character input from user
    print("Enter a guess:", end='') 
    guessChar = input()
    
    # to check the length of input given by the user
    if len(guessChar)!=0 :
        
        if len(guessChar)==1:
            
            # checking wether the input is character or integer
            if guessChar.isdigit():
                print("Invalid input! Please enter a character not numbers!")
                # if its character then passes out
                pass
            
            # isdigit else
            else:
                if guessChar.upper() in letterGuessed:
                    print()
                    print(f"You have already guessed {guessChar}. Please guess another letter.")
                    print()
                else:
                    #right condition for game starts from here
                    if guessChar.upper() in realWord:
                        print()
                        print(f"Correct! {guessChar} is the right guess!")
                        
                        print()
                    else:
                        if hangManint==7:
                            print(hangmanSkeleton[(hangManint-guessNo)+0])
                        elif hangManint == 5:
                            print(hangmanSkeleton[(hangManint-guessNo)+2])
                        elif hangManint ==3:
                            print(hangmanSkeleton[(hangManint-guessNo)+4])
                        print()
                        guessNo -= 1
                        if guessNo>0:
                            print(f"Wrong {guessChar} is the wrong guess. {guessNo} guess left!")
                            print(f"Word Hint:{hintRealWord}")
                            print()
                    
            # will append the characters the user has guessed till now to the string
            letterGuessed = letterGuessed+ guessChar.upper()
            failureCount = 0
            for alphabets in realWord:
                if guessNo>0:
                    if  alphabets in letterGuessed.upper() :
                        print(f"{alphabets}", end='')
                    else:
                        print("_ ", end='')
                        failureCount +=1
            print("")        
                        
                
            if failureCount == 0:
                print()
                print("Congrats You have won the game")
                print()
                break
                       
        # len >0 else
        else:
            print("Error! Please enter a single character!")
            
    # len 0 else
    else:
        print("Please enter a guess:")
else:       
    print()
    print("Sorry You lost the Game! ") 
    print()

