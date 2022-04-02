
from pyparsing import Word
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_IDF import weight_IDF
import numpy as np

#filling vector with zeros then at each position filling it with the IDF weight of THE PROPER term according to words_positions' values

#def augmented_vector_Full(document):
    # vector=[]
    # words_positions = countsArray(document)[0]
    # counts_Array = countsArray(document)[1]

    # for word in words_positions:
    #     #print(word)
    #     Full_weight = weight(word,0,document)
    
    #     vector.insert(words_positions[word], Full_weight) #fill vector    at position : position of word         with val : IDF_weight

    # return words_positions, vector

#method 2 : using vectors of both IF and IDF, multiply each element at same posiition of both vectors
def vector_Full(vector_TF, vector_IDF):
    vector_Full=[]
    counter = 0
    for x in vector_TF:
        full_weight = x*vector_IDF[counter]
        counter = counter + 1
        vector_Full.append(full_weight)

    return vector_Full
