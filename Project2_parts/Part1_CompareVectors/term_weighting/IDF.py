# no need for which doc : loops over all documents' arrays in countsArray to see if word occured there (value > 0)
# IDF = log(N/DF)
# Where: N is the number of documents in C, i.e., N = |C|
# DF is the number of docs in C containing at least one occurrence of term ti
import math


def IDF(word, positions_dictionnary,      countsArray):
    
    # Check if the word is in our Documents firt
    if word in positions_dictionnary.keys():
        word_position = positions_dictionnary[word]
    else:
        return 0

    document_freq = 0   #this is DF in IDF formula
    
    for array in countsArray:
        occurence_value = array[word_position]
        if (occurence_value>0): #if term is present in document
            document_freq = document_freq+1

    N = len(countsArray)
    
    IDF_formula = math.log(N/document_freq)
    
    #print("N: ", N)
    #print("DF ", document_freq)
    

    return IDF_formula