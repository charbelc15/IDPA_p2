from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.vector.Filter_Text import Filter_Text
from Project2_parts.Part1_CompareVectors.vector.acceptable_text import acceptable_text
from Project2_parts.Part1_CompareVectors.vector.vector_Full import vector_Full
from Project2_parts.Part1_CompareVectors.vector.vector_TF import vector_TF
from Project2_parts.Part1_CompareVectors.vector.vector_IDF import vector_IDF
    

#returns the TF vector of the Query
def Query_Full_vector(documents, _vector_TF, _vector_IDF):
    words_positions = vector_IDF(documents)[0] #!!!! vector_IDF here instead of vector_Full (same elements order + vector_Full only returns vector) 
    #print(words_positions)
    counts_Array = vector_Full(_vector_TF,_vector_IDF)[len(documents)-1]  # !!doc Position --> query is added bl ekhir --> len(doc)-1
    #print(counts_Array)
    Full_weights_vector=[]

    for word in words_positions:
        inner_vector=[]
        inner_vector.append(word)    

        word_position_in_counts_Array = words_positions[word]
        inner_vector.append(counts_Array[word_position_in_counts_Array])

        Full_weights_vector.append(inner_vector)


    return Full_weights_vector