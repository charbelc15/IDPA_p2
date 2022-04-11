from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.vector.Filter_Text import Filter_Text
from Project2_parts.Part1_CompareVectors.vector.acceptable_text import acceptable_text
from Project2_parts.Part1_CompareVectors.vector.vector_TF import vector_TF
    

#returns the TF vector of the Query
def Query_TF_vector(documents):
    words_positions = vector_TF(documents)[0]
    #print(words_positions)
    counts_Array = vector_TF(documents)[1][len(documents)-1]   # !!doc Position --> query is added bl ekhir --> len(doc)-1
    #print(counts_Array)
    TF_weights_vector=[]

    for word in words_positions:
        inner_vector=[]
        inner_vector.append(word)    

        word_position_in_counts_Array = words_positions[word]
        inner_vector.append(counts_Array[word_position_in_counts_Array])

        TF_weights_vector.append(inner_vector)


    return TF_weights_vector