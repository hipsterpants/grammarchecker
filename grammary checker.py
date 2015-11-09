import nltk

def main():
    print("This is a grammar checker. Enter a sentence and I will attempt to verify if it is grammatically correct")
    sentence = raw_input("Please enter a sentence: ")
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    structure = []
    j = 0
    for i in tagged:
        structure.append(i[1]) #structure is just the parts of speech in order
        j = j + 1

    print(structure) #for debugging
    
    if hasVerb(structure):
        print("Has a verb")
        if hasSubject(structure):
            print("Has a subject")
            if verbAfterSubject(structure):
                print("Verb is after subject")
                return True
    return False
            

#a list of all tag meanings: nltk.help.upenn_tagset()

verb = ["VB", "VBD", "VBN","VBP", "VBZ"]
subject = ["NN", "NNP", "NNPS", "NNS", "PRP", "VBG"]

def hasVerb(sent): # sent is an table of parts of speech
    for i in sent:
        if i in verb:
            return True
    return False

def hasSubject(sent):
    for i in sent:
        if i in subject:
            return True
    return False

def verbAfterSubject(sent):
    verbPos = 0
    subjPos = 0
    for i in sent:
        if i in verb:
            return False
        if i in subject:
            return True

nltk.help.upenn_tagset()

#while 1:
    #print(main())
