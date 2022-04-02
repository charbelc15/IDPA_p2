
from pyparsing import Word
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_IDF import weight_IDF
import numpy as np

#filling vector with zeros then at each position filling it with the IDF weight of THE PROPER term according to words_positions' values

def vector_IDF(document):
    vector=[]
    words_positions = countsArray(document)[0]
    counts_Array = countsArray(document)[1]

    for word in words_positions:
        #print(word)
        IDF_weight = weight_IDF(word,0,document)
        vector.insert(words_positions[word], IDF_weight) #fill vector    at position : position of word         with val : IDF_weight

    return words_positions, vector
