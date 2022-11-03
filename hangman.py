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

# I will randomly choose this word from a excel sheet for final drat
realWord = "HELICOPTER"
hintRealWord = " A flying thing"



# prints out the initial part of the game
print()
print("WELCOME TO HANGMAN GAME")
print("Note*")
print("You will be provided hints accross the game!")
print("The higher difficulty level will give you lee no of chances!")

print()
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
print()
print(f"Hint:{hintRealWord}")
print()
for alphabets in realWord:
    print("_ ", end='')
print()

  
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
                        print()
                        print(f"Correct! {guessChar} is the right guess!")
                        print()
                    else:
                        print(hangmanSkeleton[hangManint-guessNo])
                        print()
                        guessNo -= 1
                        print(f"Wrong {guessChar} is the wrong guess. {guessNo} guess left!")
                        print(f"Hint:{hintRealWord}")
                        print()
                    
            # will append the characters the user has guessed till now to the string
            letterGuessed = letterGuessed+ guessChar
            
            for alphabets in realWord:
                if  alphabets in letterGuessed.upper() :
                    print(f"{alphabets}", end='')
                else:
                    print("_ ", end='')
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
    
    
    
    