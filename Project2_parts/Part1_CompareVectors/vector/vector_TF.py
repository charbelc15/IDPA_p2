
from pyparsing import Word
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_TF import weight_TF

#returns vectors of TF for all docs in DOCUMENTS
def vector_TF(document):
    words_positions = countsArray(document)[0]
    counts_Array = countsArray(document)[1]

    return words_positions,counts_Array