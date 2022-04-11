
from pyparsing import Word
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray
from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_TF import weight_TF
from Project2_parts.Part1_CompareVectors.vector.Filter_Text import Filter_Text
from Project2_parts.Part1_CompareVectors.vector.acceptable_text import acceptable_text
from Project2_parts.Part1_CompareVectors.vector.vector_TF import vector_TF

#returns the augmented vector of the specified document
#Each document: 
#   Own position, 
#   Own filtered text, 
#   Own Element Properties
def augmented_vector_TF(documents, ElementProperties,docposition,Doc_filtered_text):
    words_positions = vector_TF(documents)[0]
    counts_Array = vector_TF(documents)[1][docposition]   # !!doc Position (which of C are we considering)
    TF_weights_vector=[]

    for word in words_positions:
        if not(word in Doc_filtered_text):
            TF_weights_vector.append([word, 0])         #words that are not in document ::placed first :: weight of 0

    for element in ElementProperties:
        # Step1 
        # Extract TF_val of Element's text       from counts Array (for whole DOC)

        text_val_of_element = element[3]
        text_val_of_element = text_val_of_element.lower() # node text: lau is here for you

        
        #decompose node phrase:   lau   is      here     for     you
        #Does not work if text is empty or only contains stop word
        if( acceptable_text(text_val_of_element) ):
            filtered_text_val_of_element = Filter_Text(text_val_of_element)
            inner_document = [filtered_text_val_of_element]
            node_words_filtered = countsArray(inner_document)[0] 
            
            for key in node_words_filtered: #we use the node_words_positions to get the keys : lau         is      .. free of space, /n, etc.. (just to use splitting of package)
            # I am inside node
                position_of_element_text_val_in_TF_vector = words_positions[key] # position is to be retrieved from the FULL DOC's wordspositions 
                                                                                # (NOT THE node's node_word_positions, its like every node is a DOC )
                
                TF_val = counts_Array[position_of_element_text_val_in_TF_vector] # TF_val is to be retrieved from the FULL DOC's countsArray 
                                                                                # (NOT THE node's node's countsArray, it would be like every node is a DOC )

                
                #Step 2 : Extract path factor of element         from ElementProperties
                path_factor = element[2]

                #Step 3 : Multiply them + Append them to augmented vector
                TF_weight = TF_val*path_factor
                TF_weights_vector.append([key,TF_weight])

    return TF_weights_vector