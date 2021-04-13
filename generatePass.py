import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '%', '+', '\\', '/', "'", '!', '#', '$', '^', '?', ':', '.', ')', '(', '}', '{', ']', '[', '~']

def generatePassword():
    password = ""
    passLength = input("Password length: ")
    for x in range(int(passLength)):
        randNum = random.randint(1,3)
        if randNum == 1:
            randNum = random.randint(1,2)
            if randNum == 1:
                password += letters[random.randint(0,len(letters)-1)].lower()
            elif randNum == 2:
                password += letters[random.randint(0,len(letters)-1)].upper()
        elif randNum == 2:
            password += numbers[random.randint(0,len(numbers)-1)]
        elif randNum == 3:
            password += symbols[random.randint(0, len(symbols)-1)]
    return password
            
while True:
    print(generatePassword())
    query = input("Generate another? Y/N: ")
    if query.lower() == "y" or query.lower() == "yes":
        continue
    else:
        break
    
