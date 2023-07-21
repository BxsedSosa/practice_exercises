def character_remove():
    word = str(input('What is the word youd like to use?: '))
    n = int(input('Where would you like to slice the word?: '))
    n = n - 1
    x = word[n:]
    print(x)

character_remove()