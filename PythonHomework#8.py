import os

fileTxt = ""
fileName = ""

def options():

    print("-" * 10)

    print("""
what would you like to do?:
1. Read the file
2. Delete the file and start over
3. Append the file
4. Replace single line
5. Exit
                    """)

    menuOpt = int(input("Enter the option number: "))

    if menuOpt == 1:
        fileName = str(input("Enter filename: "))
        #create function to read file
        if check_exist(fileName) == True:
            readFile(fileName)
            input("press ENTER to return to main menu")

            options()
        else:
            print(f"file {fileName} not found. Create file? Y/N ? ")
            choice = str(input(":> "))

            if choice.upper() == 'Y':
                createFile(fileName)
                print("returning to main menu... ")
                options()
            elif choice.upper() == 'N':
                print("returning to main menu... ")
                options()
            else:
                print("Invalid option, please re-enter")

        #readFile()
        #options()

    elif menuOpt == 2:
        fileName = str(input("Enter file to be deleted: "))
        if check_exist(fileName) == True:
            deleteFile(fileName)
            input("press ENTER to return to main menu")
            options()
        else:
            print(f"!!! file {fileName} not found...")
            options()

    elif menuOpt == 3:
        fileName = str(input("Enter the file to append to: "))
        if check_exist(fileName) == True:
            appendFile(fileName)
            input("press ENTER to return to main menu")

            options()
        else:
            print(f"file {fileName} not found. Create file? Y/N ? ")
            choice = str(input(":> "))

            if choice.upper() == 'Y':
                createFile(fileName)
                print("returning to main menu... ")
                options()
            elif choice.upper() == 'N':
                print("returning to main menu... ")
                options()
            else:
                print("Invalid option, please re-enter")
        options()

    elif menuOpt == 4:
        fileName = str(input("Enter the file to replace line in: "))
        if check_exist(fileName) == True:
            repTxt = str(input("enter text: "))
            repLineNbr = int(input("line to replace with text: "))
            repLine(fileName, repTxt, repLineNbr)
            input("press ENTER to return to main menu")

            options()
        else:
            print(f"file {fileName} not found. Create file? Y/N ? ")
            choice = str(input(":> "))

            if choice.upper() == 'Y':
                createFile(fileName)
                print("returning to main menu... ")
                options()
            elif choice.upper() == 'N':
                print("returning to main menu... ")
                options()
            else:
                print("Invalid option, please re-enter")

        options()

    elif menuOpt == 5:
        exit()


def repLine(fileName, repTxt, repLineNbr):
    with open(fileName,"r") as txt:
        txtLines = txt.readlines()
        for ln in txtLines:
            if txtLines.index(ln) == repLineNbr -1:
                txtLines[txtLines.index(ln)] = repTxt + "\n"
                break

    with open(fileName,"w") as txt:
        for ln in txtLines:
            txt.write(ln)

def appendFile(fileName):
    with open(fileName,"a") as txt:
        appTxt = str(input("append text: "))
        txt.writelines(appTxt + "\n")

    options()

def deleteFile(fileName):
    os.remove(fileName)
    print(f"file {fileName} has been removed")

def createFile(fileName):
    with open(fileName,"w") as txt:
        print(f"file {fileName} has been created")

def readFile(fileName):
    with open(fileName,"r") as fileTxt:
        txt = fileTxt.read()
        print(txt)

def check_exist(fileName):
    if os.path.exists(fileName) == True:
        print(f"file {fileName} exists in {os.path.abspath(fileName)}")
        return True
    else:
        return False


options()
