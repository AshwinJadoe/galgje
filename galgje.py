import random
wordlist = ["apple"]
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
blanks = []
lives = 6
game = True
chosenletters = []
instructions = "You can use the following commands: \n lives: shows the amount of lives you have left \n letters: shows the letters you have already chosen \n type help to see the instructions again\n \n"
print(instructions)
word = list(random.choice(wordlist))
for i in range(len(word)):
    blanks.append("_")



def lettercheck(choice):
    if choice not in alfabet:
        print("please only choose single letters")
        return False
    if choice in chosenletters:
        print("you have already chosen this letter")
        return False
    return True

def controlcheck(choice):
    if choice == "lives":
        print("you have {} lives left\n".format(lives))
        return True
    if choice == "letters":
        print("You have already chosen the following letters: \n", ' '.join(map(str, chosenletters)))
        return True
    if choice == "help":
        print(instructions)
        return True

def galgje(wordlist, word, lives, game):
    if lives == 0:
        game = False
        win = True
    if "_" not in blanks:
        game = False
        win = False
    if game == True:
        choice = input("What will be your next letter? ").lower()
        if controlcheck(choice):
            galgje(wordlist, word, lives, game)
        if lettercheck(choice):
            chosenletters.append(choice)
            if choice in word:
                for i in range(len(word)):
                    if choice in word:
                        if word[i] == choice:
                            blanks[i] = choice
                print(' '.join(map(str, blanks)))
                galgje(wordlist, word, lives, game)
            else:
                print("That letter is not in the word!")
                print(' '.join(map(str, blanks)))
                lives -= 1
                galgje(wordlist, word, lives, game)
    else:
        if win == True:
            print("Great job you beat the gam! \n You have {} lives left". format(lives))
        elif win == False:
            print("Too bad you have run out of lives and lost the game \n your word was: ", "".join(map(str, word)))




galgje(wordlist, word, lives, game)
