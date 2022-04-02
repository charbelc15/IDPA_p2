from Project2_parts.Part1_CompareVectors.term_weighting.TF import TF
from Project2_parts.Part1_CompareVectors.term_weighting.IDF import IDF
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray

def weight_IDF(word, doc, documents):
    
    
    words_positions = countsArray(documents)[0]
    counts_Array = countsArray(documents)[1]

    return IDF(word, words_positions, counts_Array)

