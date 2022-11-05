
# Fjodor/Lexaia

vocals = ["a","e","i","o","u"]
def getPrevLast(vocals: list): #
    if len(vocals) >= 2:
        return vocals[-2]
    return vocals[0]

def getVocalGroups(word: str): #get all "vocalGroups" -> chains of vocals (aeiou)
    vocalGroups = []
    vocalGroup = ""
    for i in range(len(word)):
        letter = word[i]
        if vocals.count(letter):
            vocalGroup += letter
        elif vocalGroup != "":
            vocalGroups.append((vocalGroup,i-len(vocalGroup)))
            vocalGroup = ""
        pass
    return vocalGroups
def getLettersAfterI(word:str,index:int):
    return "".join(word[i] for i in range(index,len(word)))

def getPercentageOfStrigString(word1:str,word2:str):
    lettersWord1 = []
def compareWord(word1: str,word2:str):
    tests = []
    VocalGrupsWord1 = getVocalGroups(word1)
    VocalGrupsWord2 = getVocalGroups(word2)
    PrevLastWord1 = getPrevLast(VocalGrupsWord1)
    PrevLastWord2 = getPrevLast(VocalGrupsWord2)
    LastLetters1 = getLettersAfterI(word1,PrevLastWord1[1])
    LastLetters2 = getLettersAfterI(word2, PrevLastWord2[1])
    tests.append(PrevLastWord1[0] == PrevLastWord2[0])

    return {
        "VocalGroupTest":tests[0],
    }
print(compareWord("breitschlagen","bapfel"))
