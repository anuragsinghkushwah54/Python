#Python code to check if a given character is vowel or consonant.
chare=input("please enter a character :")
for i in chare:
    if i == "a" or "e" or "i" or "u" or "A" or "E" or "I" or "O" or "U":
        print(i,"is vowel")
    else:
        print(i,"is not vowel")