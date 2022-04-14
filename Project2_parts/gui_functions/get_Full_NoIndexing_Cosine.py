from typing import OrderedDict
import xml.etree.ElementTree as ET
from Project2_parts.Part1_CompareVectors.vector.augmented_vector_Full import augmented_vector_Full
from Project2_parts.Part1_CompareVectors.vector.augmented_vector_IDF import augmented_vector_IDF
from Project2_parts.Part1_CompareVectors.vector.augmented_vector_TF import augmented_vector_TF
from Project2_parts.Part1_CompareVectors.vector.getDocFullText import getDocFullText

from Project2_parts.Part1_CompareVectors.vector.getPathFactor import getPathFactor
from Project2_parts.Part1_CompareVectors.vector.Filter_Text import Filter_Text
from Project2_parts.Part1_CompareVectors.vector.vector_IDF import vector_IDF
from Project2_parts.Part1_CompareVectors.vector.vector_TF import vector_TF
from Project2_parts.Part1_CompareVectors.vector_average.Cosine import Cosine
from Project2_parts.Part1_CompareVectors.vector_average.PCC import PCC
from Project2_parts.Part1_CompareVectors.vector_tools.vector_to_dict import vector_to_dict
from Project2_parts.Part2_Indexing.docID import docID
from Project2_parts.Part2_Indexing.index_Query_Full import index_Query_Full
from Project2_parts.Part2_Indexing.index_Query_IDF import index_Query_IDF
from Project2_parts.Part2_Indexing.index_Query_TF import index_Query_TF
from Project2_parts.Part2_Indexing.order_docs import order_docs
from Project2_parts.Part2_Indexing.split_query import split_query
from Project2_parts.Part3_UserInputs.Query_Full_Vector import Query_Full_vector
from Project2_parts.Part3_UserInputs.Query_IDF_vector import Query_IDF_vector
from Project2_parts.Part3_UserInputs.Query_TF_vector import Query_TF_vector
import os
import operator

def get_Full_NoIndexing_Cosine(strings,Query):

    Similarities={}
        #1. Augmented Vectors
        #1.1 Element Properties of each doc
    counter = 1

    documents=[]
    All_ElementProperties=[]
    All_Filtered_Texts=[]

    for string1 in strings:
        tree1 = ET.parse(string1)
        tree_root1 = tree1.getroot()


        flagcounter3 = 0
        for i in tree_root1.iter(): 
            flagcounter3+=1

        # Fill ElementProperties to get the path factor according to depth
        ElementProperties=[]
        flag3 = [False]*flagcounter3
        getPathFactor(tree_root1,flag3,0,False,ElementProperties) 
        print()
        print("doc ", counter," 's Element Properties : ", ElementProperties)

            #1.2 get Full text of Document
        # Get the *Filtered Full Text* of Doc1 to produce term weighting TF / IDF / Full

                #1.2.1 pass over all doc and add text values to a list : text
        flagcounter4 = 0
        for i in tree_root1.iter(): 
            flagcounter4+=1

        text=[]
        flag4 = [False]*flagcounter4
        getDocFullText(tree_root1,flag4,0,False,text)
        print()

                #1.2.2 Convert the list text to a String doc "Full text"
        FullText=""
        for text_val in text:
            #FullText+= text_val.split('\n')[0] + " "
            FullText+= text_val + " "

                #1.2.3 filter Fulltext values from stop words : i, a, special char, \n...
        Filtered_Text = Filter_Text(FullText)
        print("doc ", counter," 's Filtered Text : ", Filtered_Text)

        counter+=1
        documents.append(Filtered_Text)
        All_ElementProperties.append(ElementProperties)
        All_Filtered_Texts.append(Filtered_Text)

        #1.3 Get augmented TF vector
    # documents.append("Charbel LIU")
    # documents.append("aub ece john")
    # documents.append("no words here")
    counter=0
    #All_aug_vectors_TF=[]
    #All_aug_vectors_IDF=[]
    All_aug_vectors_Full=[]










    #Query
    documents.append(Query)












    for i in range(len(All_Filtered_Texts)):

        # Get parameters for functions
        ElementProperties = All_ElementProperties[counter]
        Filtered_Text = All_Filtered_Texts[counter]

        # Get TF aug vector of each doc
        #aug_vector_TF_1 = augmented_vector_TF(documents,ElementProperties,counter,Filtered_Text)

            # Get IDF aug vector of each doc
        #aug_vector_IDF_1 = augmented_vector_IDF(documents,ElementProperties,counter,Filtered_Text)

            # Get Full aug vector of each doc
        _vector_TF_1 = vector_TF(documents)[1]
        _vector_IDF_1 = vector_IDF(documents)[1]
        aug_vector_Full_1 = augmented_vector_Full(documents,ElementProperties,counter,Filtered_Text,_vector_TF_1,_vector_IDF_1)

        # Get Dictionary of each aug vector
       # TF_dict1 = vector_to_dict(aug_vector_TF_1)
       # IDF_dict1 = vector_to_dict(aug_vector_IDF_1)
        Full_dict1 = vector_to_dict(aug_vector_Full_1)

        # Append Dictionaries aug vector of each doc
        #All_aug_vectors_TF.append(TF_dict1)
        #All_aug_vectors_IDF.append(IDF_dict1)
        All_aug_vectors_Full.append(Full_dict1)

        # UPDATE COUNTER AT END OF LOOP
        counter+=1 #!!!!!!!!!!!!!!!
        


    print()
    print("augmented Full vectors: \n")
    print()
    print("AugFull Doc1 \n", (All_aug_vectors_Full[0]))
    print()
    print("AugFull Doc2 \n", (All_aug_vectors_Full[1]))
    print()
    print("AugFull Doc3 \n", (All_aug_vectors_Full[2]))
    print()
    print("AugFull Doc4 \n", (All_aug_vectors_Full[3]))
    print()
    print("AugFull Doc5 \n", (All_aug_vectors_Full[4]))
    print()
    print("AugFull Doc6 \n", (All_aug_vectors_Full[5]))
    print()
    print("AugFull Doc7 \n", (All_aug_vectors_Full[6]))
    print()
    print("AugFull Doc8 \n", (All_aug_vectors_Full[7]))
    print()
    print("AugFull Doc9 \n", (All_aug_vectors_Full[8]))
    print()
    print("AugFull Doc10 \n", (All_aug_vectors_Full[9]))
    print()


    # query vector Full
    Q_vector_TF_1 = vector_TF(documents)[1]
    Q_vector_IDF_1 = vector_IDF(documents)[1]
    Full_Query = Query_Full_vector(documents, Q_vector_TF_1, Q_vector_IDF_1)  # vector
    Full_Query_dict = vector_to_dict(Full_Query)                              # dict
    print()
    print("Full Query dictionary \n")
    print((Full_Query_dict))
    

    # Similarities comparison via Cosine
    print("Similarity via Cosine with Doc1 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[0] ) )
    print("Similarity via Cosine with Doc2 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[1] ) )
    print("Similarity via Cosine with Doc3 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[2] ) )
    print("Similarity via Cosine with Doc4 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[3] ) )
    print("Similarity via Cosine with Doc5 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[4] ) )
    print("Similarity via Cosine with Doc6 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[5] ) )
    print("Similarity via Cosine with Doc7 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[6] ) )
    print("Similarity via Cosine with Doc8 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[7] ) )
    print("Similarity via Cosine with Doc9 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[8] ) )
    print("Similarity via Cosine with Doc10 : ", Cosine( Full_Query_dict , All_aug_vectors_Full[9] ) )

    #Filling Similarities

    counter = 0
    for string in strings: 
        #Get File name
        head_tail = os.path.split(string)
        file_name = head_tail[1]
        
        #Key: File Name
        #Value : Similarity
        Similarities[file_name] = Cosine( Full_Query_dict , All_aug_vectors_Full[counter] )
        counter+=1

    #Order Similarities
    Similarities = dict( sorted(Similarities.items(), key=operator.itemgetter(1),reverse=True))
    print()
    print("Ordered Similarities")
    print(Similarities)