
from pyparsing import Word
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_IDF import weight_IDF
import numpy as np
#returns vectors of IDF for all docs in DOCUMENTS
#filling vector with zeros then at each position filling it with the IDF weight of THE PROPER term according to words_positions' values

def vector_IDF(documents):
    full_vector = []
    # for doc in documents: 
    #     full_vector.append(0)
    words_positions = countsArray(documents)[0]
    counts_Array = countsArray(documents)[1]

    for doc in documents:
        inner_vector=[]

        for word in words_positions:
            #print(word)
            IDF_weight = weight_IDF(word,0,documents)
            inner_vector.insert(words_positions[word], IDF_weight) #fill vector    at position : position of word         with val : IDF_weight
        full_vector.append(inner_vector)

    return words_positions, full_vector
