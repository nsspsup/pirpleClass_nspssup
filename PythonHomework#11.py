import sys, os, time, platform, random
import urllib.request, urllib.error



guessed_letters = set([])
word = ""
remaining_letters = 100
guess = ""
wrong_guess_cnt = 0

class Player:
    def __init__(self,name = "name", game_role = ""):
        self.name = name
        self.game_role = game_role



def screenClear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def draw_gallows_map(wrong_guess_cnt):
    map = [
        [3,3,3,3,3,3,0,0],
        [2,0,0,0,0,4,0,0],
        [2,0,0,0,0,5,0,0],
        [2,0,0,0,6,7,8,0],
        [2,0,0,9,0,10,0,11],
        [2,0,0,0,12,0,13,0],
        [2,0,0,14,0,0,0,15],
        [2,0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1,1]
            ]
    build_seq = {
        0:" ",
        1:"=",
        2:"|",
        3:"-",
        4:"|",
        5:"O",
        6:"/",
        7:"|",
        8:"\ ",
        9:"|",
        10:"|",
        11:"|",
        12:"/",
        13:"\ ",
        14:"|",
        15:"|"
    }


    sequence = wrong_guess_cnt
    #build gallow and hangman

    if len(build_seq) == wrong_guess_cnt:
        print("YOU LOSE")
        print("the word was:", word)
        exit()


    for y in map:

        for x in y:
            if x <= sequence:
                print(build_seq[x],end="")
        print()

Player1 = Player()
Player2 = Player()

def define_player_names():
    print(
""" 
1. single player 
or 
2. two player game
""")
    choice = input(">>>: ")
    if choice == "1":
        Player1.name = input("Enter your name: ")
        Player1.game_role = "hangman"
        single_player_game()
    elif choice == "2":
        print("Set players and roles")
        print("---------------------")
        Player1.name = input("Player 1 name: ")
        Player2.name = input("Player 2 name: ")
        define_player_roles()
    else:
        print("invalid choice, try again.")
        define_player_names()

def define_player_roles():
    print("---------------------")
    print("Executioner ","1:",Player1.name,"2:",Player2.name)
    choice = str(input(">>>: "))

    if choice == "1":
        Player1.game_role = "executioner"
        Player2.game_role = "hangman"
    elif choice == "2":
        Player2.game_role = "executioner"
        Player1.game_role = "hangman"
    else:
        print("invalid choice, try again ")
        define_player_roles()

    two_player_game()

def draw_guess_row(word,guessed_letters):
    screenClear()
    global remaining_letters
    size = len(word)
    remaining_letters = size
    letters = [] # word to be guessed entered by executioner
    print()
    for i in word:
        letters.append(i)

    #replace letters that are not guessed by "_"
    displayed_letters = letters

    for i in displayed_letters:
        if i in guessed_letters:
            print(i +" ",end = "")
            remaining_letters -= 1
        else:
            print("_ ", end = "")

    print()
    print("Already used letters:", sorted(guessed_letters))

def two_player_game():
    global word
    if Player1.game_role == "executioner":
        executioner = Player1.name
    else:
        executioner = Player2.name

    print(executioner,"enter your word: ")
    word = input(">>>: ").upper()

    print(word)
    time.sleep(1)
    screenClear()

    play()

def single_player_game():
    global word
    try:
        url = "https://raw.githubusercontent.com/nsspsup/pirpleClass_nspssup/master/wordlist.txt"
        print("wordlist download started!")
        filename, headers = urllib.request.urlretrieve(url,filename="wordlist.txt")
        print("wordlist download complete!")

        with open("wordlist.txt","r") as mywords:
            lines = mywords.readlines()
            randline = random.choice(lines)
            word = randline.strip("\n").upper()
            #print(word)
        play()
    except urllib.error.URLError as e:
        print(e.reason)
        print()

        print("""
Unable to download wordlist. 

If your internet connection works fine other reasons can be connection over proxy or VPN  

continue in 2 player mode? Y/N
""")
        choice = input(">>>:").lower()
        if choice == "y":
            define_player_names()
        elif choice == "n":
            print("exiting game...")
        else:
            print("invalid choice, try again")
            single_player_game()
            
    except Exception as e:
        print(e)

def make_guess():
    global guess
    print()
    if Player1.game_role == "hangman":
        print(f"{Player1.name} make a guess")
        guess = input(">>>: ").upper()
        if guess in guessed_letters:
            print("letter already used, choose again")
            make_guess()
        elif guess == "":
            print("No letter was typed, please try again")
            make_guess()
        elif len(guess) > 1:
           print("Enter only 1 letter per guess, try again")
           make_guess()
        else:
            guessed_letters.add(guess)

        guessed_letters.add(guess)
    elif Player2.game_role == "hangman":
        print(f"{Player2.name} make a guess")
        guess = input(">>>: ").upper()
        if guess in guessed_letters:
            print("letter already used, choose again")
            make_guess()
        else:
            guessed_letters.add(guess)


def play():
    global wrong_guess_cnt

    while remaining_letters > 0:

        remaining_letters_antes = remaining_letters
        make_guess()
        draw_guess_row(word, guessed_letters)
        if remaining_letters_antes == remaining_letters:
            wrong_guess_cnt += 1

        elif remaining_letters == 0:
            print(" YOU WIN ")
        draw_gallows_map(wrong_guess_cnt)

define_player_names()


