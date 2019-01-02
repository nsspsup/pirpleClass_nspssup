import sys
from termcolor import colored, cprint

columns = 7
rows = 6
currentPlayer = '1'
player = {"1":"red","2":"green"}
moves =[]



#generate blank list of player moves
def gen_blank():
    global moves
    sublist =[]
    for row in range(6):
        sublist = []
        for row in range(7):
            sublist.append(" ")
        moves.append(sublist)



# creates values 0 - 41 in the moves lists. Intended only for testing of flipping and winning check functions
def gen_numbers():
    global moves
    sublist =[]
    counter = 0
    for row in range(6):
        sublist = []
        for row in range(7):
            sublist.append(counter)
            counter += 1
        moves.append(sublist)

    for i in moves:
        print(i)

def draw_field():

    print(" 1 2 3 4 5 6 7")
    for row in range(rows*2):
        for column in range(columns*2+1):

            if row % 2 == 1:

                if column == len(range(columns * 2 )):
                    print("-")
                else:
                    print("-", end="")

            else:
                if column%2 ==0:
                    if column == len(range(columns*2)):
                        print("|")
                    else:
                        print("|",end="")
                else:
                    if row%2 == 0:
                        writeableRow = int(row/2)
                        writeableCol = int((column-1)/2)
                        if moves[writeableRow][writeableCol] != " ":
                            text = colored(" ",player[moves[writeableRow][writeableCol]],attrs=["reverse"])
                            print(text,end="")
                        else:
                            print(" ", end="")

def make_choice():
    global choice
    choice = int(input(">>>: ")) - 1
    while choice < 0 or choice >6:
        print("value must be between 1 and 7")
        print(type(choice))
        make_choice()
    return choice

def player_move():

    global currentPlayer
    text = colored((player[currentPlayer] + " player's move. Choose column 1 - 7"),player[currentPlayer])
    print(text)
    user_choice = make_choice()

    store_moves(currentPlayer,user_choice)
    if currentPlayer == "1":
        currentPlayer = "2"
    elif currentPlayer == "2":
        currentPlayer = "1"


def store_moves(currentPlayer,choice):

    global moves
    row = len(moves) - 1
    while row >= 0:
        if moves[row][choice] == " ":
            moves[row][choice] = currentPlayer
            break
        row -= 1


#check for 4 tiles in a sublist
def check_horizontal(moves_list):
    check_winner(moves_list)

#check for vertically "connected" 4 tiles
def check_vertical(moves_list):

    templist = []
    sublist = []
    row = 0
    column = 0

    for column in range(len(moves_list[row])):
        sublist=[]
        for row in range(len(moves_list)):
            sublist.append(moves_list[row][column])
        templist.append(sublist)

    check_winner(templist)

#diagonal check, goes through half of moves diagonaly, to check the other half, supply reverted (flipped) moves list
def check_diag(moves_list):
    out_list = []
    sublist = []
    size_x = len(moves_list[0]) -2
    size_y = len(moves_list)-1

    #traverse diagonally from left_up to right-middle
    boundary_x = 0
    boundary_y = 0
    for i in range(size_x):
        boundary_x += 1
        #set boundary values to size values to avoid running outside of list index
        if boundary_x >= size_x:
            boundary_x = size_x
        if boundary_y >= size_y:
            boundary_y = size_y

        tmp_x = boundary_x
        tmp_y = boundary_y
        #print("-" * 4)
        sublist = []
        while tmp_x >= 0:
            #print(moves[tmp_x][tmp_y])
            sublist.append(moves_list[tmp_x][tmp_y])
            tmp_x -= 1
            tmp_y += 1

        #add only lists that have 4 or more elements, lists with less elements do not contain winning match of player tiles
        if len(sublist) > 3:
            out_list.append(sublist)
    return out_list


#flip user moves list to use in diagonal check
def flip_horizontal(moves_list):
    temp = []
    subtemp = []

    #flip along vertical axis
    for i in moves_list:
        k = len(moves_list[moves_list.index(i)])-1
        subtemp =[]
        while k >= 0:
            subtemp.append(moves[moves.index(i)][k])
            k -= 1
        temp.append(subtemp)

    # for i in temp:
    #     print(i)
    return temp

#flip user moves list to use in diagonal check
def flip_vertical(moves_list):
    temp = []
    #flip along horizontal axis
    l = len(moves_list) -1
    while l >= 0:
        temp.append(moves_list[l])
        l -= 1

    # for i in temp:
    #     print(i)

    return temp

#check for winning combination in a list of lists.
def check_winner(evaList):
    cntPlayer1 = 0
    cntPlayer2 = 0

    for row in evaList:
        for field in row:
            if field == "1":
                cntPlayer1 += 1
            else:
                cntPlayer1 = 0

            if field == "2":
                cntPlayer2 += 1
            else:
                cntPlayer2 = 0

            if cntPlayer1 == 4:
                text = colored("CONGRATS !!! Player 1 has won the game", "red",attrs=["bold"])
                print(text)
                exit()
            if cntPlayer2 == 4:
                text = colored("CONGRATS !!! Player 2 has won the game", "green",attrs=["bold"])
                print(text)
                exit()



def play():
    while True:
        player_move()
        draw_field()
        vertical_flip = flip_vertical(moves)
        horizontal_flip = flip_horizontal(moves)
        vert_hor = flip_vertical(flip_horizontal(moves))
        check_horizontal(moves)
        check_vertical(moves)
        check_winner(check_diag(moves))
        check_winner(check_diag(vert_hor))
        check_winner(check_diag(vertical_flip))
        check_winner(check_diag(horizontal_flip))


gen_blank()
draw_field()
play()
