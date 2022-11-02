# Imports


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




# functions

def diffLevel (diffvalue):
    diffLevel = diffvalue
    capdiffLevel1 = diffLevel.upper()
    return capdiffLevel1



# Initialization and declarations

letterGuessed = " "
failureCount = 0
hangManint = 0

#guess word picked randomly form the file

realWord = "HELICOPTER"
hintRealWord = " A flying thing"



# prints out the initial part of the game
print()
print("Welcome to the hangman game")


# choosing the difficulty level
print("Choose the level of difficulty (L, M, H): " , end='')
userInput = input()
capdiffLevel = diffLevel(userInput)

# sets the difficulty level for the user

while (capdiffLevel!= "L" or capdiffLevel!="M" or capdiffLevel!="H"):
    if (capdiffLevel== "L"):
        guessNo = 7
        break
    elif (capdiffLevel== "M"):
        guessNo = 5
        break
    elif (capdiffLevel== "H"):
        guessNo = 3
        break
    else:
        print("Enter the correct input from the option")
        print("Choose the level of difficulty (L, M, H): ", end='')
        insidelevel = input()
        capdiffLevel = diffLevel(insidelevel)
    
# Game begins
hangManint= guessNo
while (guessNo>0):
   
    # Taking character input from user
    print("Enter a guess:", end='') 
    guessChar = input()
    
    # to check the length of input given by the user
    if len(guessChar)!=0 :
        
        if  len(guessChar)==1:
            
            # checking wether the input is character or integer
            if guessChar.isdigit():
                
                print("Invalid input! Please enter a character not numbers!")
                # if its character then passes out
                pass
            
            # isdigit else
            else:
                if guessChar.upper() in letterGuessed:
                    print(f"You have already guessed {guessChar}. Please guess another letter.")
                else:
                    #right condition for game starts from here
                    if guessChar.upper() in realWord:
                        
                        print(f"Correct! {guessChar} is the right guess!")
                
                    else:
                        print(hangmanSkeleton[hangManint-guessNo])
                        guessNo -= 1
                        print(f"Wrong {guessChar} is the wrong guess. {guessNo} guess left!")
                        print("Hint:", end="")
                        print(hintRealWord)
                    
            # will append the characters the user has guessed till now to the string
            letterGuessed = letterGuessed+ guessChar
            
            for alphabets in realWord:
                if  alphabets in letterGuessed.upper() :
                    print(f"{alphabets}", end='')
                else:
                    print("_", end='')
                    failureCount +=1
            print("")        
                        
                
            if failureCount == 0:
                    print("Congrats You have won the game")
                    break
                
                       
        # len >0 else
        else:
            print("Error! Please enter a single character!")
            
    # len 0 else
    else:
        print("Please enter a guess:", end='')
    
    
    
    