# word is charbel
# word_position is 0
# doc is 0 : the position of the document in countsArray:  position in counts array is 0

# positions dictionnary
# {'my': 4, 'name': 5, 'is': 2, 'charbel': 0, 'yes': 9, 'it': 3, 'no': 6, 'dont': 1, 'think': 8, 'so': 7}

# counts Array
# [[2 0 2 1 1 1 0 0 0 1]
#  [1 0 1 0 1 1 0 0 0 0]
#  [0 1 0 0 0 0 1 1 1 0]]

#TF is the term frequency of a word in its specific document
def TF(word, positions_dictionnary,      countsArray, doc):

    # Check if the word is in our Documents firt
    if word in positions_dictionnary.keys():
        word_position = positions_dictionnary[word]
    else:
        return 0

    word_position = positions_dictionnary[word]
    #print("word_position: " , word_position)

    term_frequency = countsArray[doc][word_position] 

    return term_frequency