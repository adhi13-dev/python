def countWordsFromFile():
    filename = input("enter the file name::")
    no_words = 0
    file = open(filename,"r")
    for line in file:
        words = line.split()
        no_words = no_words + len(words)
    print("number of words is " + str(no_words))
countWordsFromFile()