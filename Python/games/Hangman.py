from os import replace
import random
import re

# Variables 
# Ouvrir le fichier texte et mettre dans la variable mots
with open("english3.txt", "r") as file:
    allText = file.read()
    mots = list(map(str, allText.split()))

hanged = random.choice(mots)
length = len(hanged)

# Replace letters function
def repl(m):
    return '#' * len(m.group())

hidden = re.sub(hanged , repl, hanged)


print(hanged)
print(length)
print(hidden)


for x in range(length + 5):
    guess = input("Deviner une lettre du mot: ")
    for x in range(length):
        if guess == hanged[x]:
            hidden = re.sub(hidden, guess * hidden[x], hidden)
            print(hidden)

