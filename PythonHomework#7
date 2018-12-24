
myFavorite = {'Artist':'Pearl Jam', 'Album':'Ten', 'Released':'1991', 'Duration_minutes':'5', 'Duration_seconds':'40'}

for key in myFavorite:
    print(key + " <> " + str(myFavorite[key]))

def guess(property,value):
    match = False
    for k in myFavorite:
        if k.lower() == property and myFavorite[k].lower() == value:
            match = True

    if match == True:
        return True
    else:
        return False

while True:
    print("-----------------------")
    guess_key = input("Enter dictionary key: ").lower()
    guess_value = input("Enter the key value: ").lower()

    print(guess(guess_key, guess_value))
