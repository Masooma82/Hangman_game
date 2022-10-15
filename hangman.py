# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 13:21:33 2022

@author: AMC
"""

import random

w = 'words.txt'
def load_words():
    print("Loading word list from file...")
   
    inFile = open(w,'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ",len(wordlist),"words loaded.")
    return wordlist
   
wordlist = load_words()

def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word,letters_guessed):
    for x in secret_word:
        if x not in letters_guessed:
            return "False"
            break
    return "True"
    

def get_guessed_word(secret_word,letters_guessed):
    L = [0]*len(secret_word)
    for x in range(len(letters_guessed)):
        for a in range(len(secret_word)):
            if secret_word[a] == letters_guessed[x]:
                L[a] = letters_guessed[x]
    for y in range(len(L)):
        if L[y] == 0:
            L[y]= "_ "
                    
            
    s = ("".join(L))
    return s
           
    


def get_available(letters_guessed):
    L1 = []
    import string as s
    s = s.ascii_lowercase
    for x in s:
        if x not in letters_guessed:
            L1.append(x)
            
    s1 = ''.join(L1)
           
    return s1

def hangman(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    print("You have",warnings_remaining,"warnings left")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
    
    letters_guessed = [] 
    available_letters = get_available(letters_guessed)
   
    g = ["_ "]*len(secret_word) 
    g = ''.join(g)
    
    L3 = [] #for counting unique elements
    for x in secret_word:
        if x not in L3:
            L3.append(x)
    count_of_unique_letters = len(L3)
            
            
    while guesses_remaining != 0 and guesses_remaining > 0:
        print("You have",guesses_remaining,"guesses left")
        print("Available letters:",available_letters)
        guess = input("Please guess a letter:")
        guess = str.lower(guess)
      
        i = str.isalpha(guess)
        if i == 0 :
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops!That letter is not a valid letter.You have no warnings left so you lose one guess:",g)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
            else:
                warnings_remaining -= 1
                print("Oops!That letter is not a valid letter.You have",warnings_remaining,"warnings left:",g)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
        elif guess in letters_guessed:
            if warnings_remaining == 0:
                guesses_remaining -= 1
                print("Oops!You'have already guessed that letter no warnings left so you lose one guess:",g)
             
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
            else:
                warnings_remaining -= 1
                print("Oops!You'have already guessed that letter",warnings_remaining,"warnings left:",g)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")        
                
        else:
            letters_guessed.append(guess)
            available_letters = get_available(letters_guessed)
            g = get_guessed_word(secret_word,letters_guessed)
            if guess in secret_word:
                print("Good guess:",g)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
            else:
                print("Oops!That letter is not in my word",g)
                print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
                if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
           
                    
            f = is_word_guessed(secret_word,letters_guessed)
            if f == "True":
                print("Congratulations,you won!")
                print("Your total score is:",guesses_remaining*count_of_unique_letters)
                break
    else:
        print("Sorry,you ran out of guesses.The word was else.")
#secret_word = choose_word(wordlist)
#hangman(secret_word)


        
def match_with_gaps(my_word,other_word):
    my_word = my_word.replace(" ","")
   
    
    if len(my_word) == len(other_word): 
        for x in range(len(my_word)):
            if my_word[x] != '_':
                if my_word[x] != other_word[x]:
                    return 'False'
                    break
   
        return "True"
                        
    else:
        return "False"

def show_possible_matches(my_word):
    L = []
    y = 0
    for x in wordlist:
        other_word = x
        r =  match_with_gaps(my_word,other_word)
        if r == 'True':
            L.append(other_word)
            
            y += 1
    if y != 0:
        print("Possible word matches are:")
        print(" ".join(L))
    else:
        print("No matches found")
   
def hangman_with_hints(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long")
    print("You have",warnings_remaining,"warnings left")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
    
    
    letters_guessed = []
    available_letters = get_available(letters_guessed)
   
    my_word = ["_ "]*len(secret_word) 
    my_word = ''.join(my_word)
    
    L3 = [] #for counting unique elements
    for x in secret_word:
        if x not in L3:
            L3.append(x)
    count_of_unique_letters = len(L3)
    while guesses_remaining != 0 and guesses_remaining > 0:
        print("You have",guesses_remaining,"guesses left")
        print("Available letters:",available_letters)
        guess = input("Please guess a letter:")
        if guess == '*':
           print(my_word)
           show_possible_matches(my_word)
           print("_ _ _ _ _ _ _ _ _ _")
            
            
            
        else:    
            guess = str.lower(guess)
          
            i = str.isalpha(guess)
            if i == 0 :
                if warnings_remaining == 0:
                    guesses_remaining -= 1
                    print("Oops!That letter is not a valid letter.You have no warnings left so you lose one guess:",my_word)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
                else:
                    warnings_remaining -= 1
                    print("Oops!That letter is not a valid letter.You have",warnings_remaining,"warnings left:",my_word)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
            elif guess in letters_guessed:
                if warnings_remaining == 0:
                    guesses_remaining -= 1
                    print("Oops!You'have already guessed that letter no warnings left so you lose one guess:",my_word)
                 
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
                else:
                    warnings_remaining -= 1
                    print("Oops!You'have already guessed that letter",warnings_remaining,"warnings left:",my_word)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")        
                    
            else:
                letters_guessed.append(guess)
                available_letters = get_available(letters_guessed)
                my_word = get_guessed_word(secret_word,letters_guessed)
                if guess in secret_word:
                    print("Good guess:",my_word)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
                else:
                    print("Oops!That letter is not in my word",my_word)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    if guess == 'a' or guess == 'e' or guess == 'i' or guess == 'o' or guess == 'u':
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
               
                        
                f = is_word_guessed(secret_word,letters_guessed)
                if f == "True":
                    print("Congratulations,you won!")
                    print("Your total score is:",guesses_remaining*count_of_unique_letters)
                    break
    else:
        print("Sorry,you ran out of guesses.The word was else.")
               
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)




        
        
       
        
        
        

        



