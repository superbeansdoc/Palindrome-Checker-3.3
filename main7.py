list = []
word = (input("type a word if you think it is a paldrome"))
wordlen = len(word)
def checkdrome(word):
    for i in range (wordlen,1,-1):
        while(True):
            if i == len(list):
                break
            else:
                lenlist = len(list)
            list.append(word[i - 1 - lenlist])
        gosh = "".join(list)
        if gosh == word:
            print("paldrome")
            break
        else:
            print("not a paldrome")
            break
checkdrome(word)