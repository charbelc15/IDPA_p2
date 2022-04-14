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

def get_IDF_Indexing_Cosine(strings,Query):

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
    All_aug_vectors_IDF=[]
    #All_aug_vectors_Full=[]










    #Query
    documents.append(Query)












    for i in range(len(All_Filtered_Texts)):

        # Get parameters for functions
        ElementProperties = All_ElementProperties[counter]
        Filtered_Text = All_Filtered_Texts[counter]

        # Get TF aug vector of each doc
        #aug_vector_TF_1 = augmented_vector_TF(documents,ElementProperties,counter,Filtered_Text)

            # Get IDF aug vector of each doc
        aug_vector_IDF_1 = augmented_vector_IDF(documents,ElementProperties,counter,Filtered_Text)

            # Get Full aug vector of each doc
        # _vector_TF_1 = vector_TF(documents)[1]
        # _vector_IDF_1 = vector_IDF(documents)[1]
        # aug_vector_Full_1 = augmented_vector_Full(documents,ElementProperties,counter,Filtered_Text,_vector_TF_1,_vector_IDF_1)

        # Get Dictionary of each aug vector
       # TF_dict1 = vector_to_dict(aug_vector_TF_1)
        IDF_dict1 = vector_to_dict(aug_vector_IDF_1)
       # Full_dict1 = vector_to_dict(aug_vector_Full_1)

        # Append Dictionaries aug vector of each doc
      #  All_aug_vectors_TF.append(TF_dict1)
        All_aug_vectors_IDF.append(IDF_dict1)
      #  All_aug_vectors_Full.append(Full_dict1)

        # UPDATE COUNTER AT END OF LOOP
        counter+=1 #!!!!!!!!!!!!!!!
        

    Keywords = split_query(Query)

    # remove query from repository to search from
    QueryDocs=[]
    for doc in documents:
        QueryDocs.append(doc)
    QueryDocs.remove(Query)

    #return dict : 
        # keys: (String) keyword 
        # values : (dictionary) docIDs where keyword is , weight of the word at that doc
    # keywords_docIDs_TF = index_Query_TF(Keywords,QueryDocs,All_aug_vectors_TF)
    # print("keywords, doc, weight TF : ",keywords_docIDs_TF)

    keywords_docIDs_IDF = index_Query_IDF(Keywords,QueryDocs,All_aug_vectors_IDF)
    print("keywords, doc, weight IDF : ",keywords_docIDs_IDF)

    # keywords_docIDs_Full = index_Query_Full(Keywords,QueryDocs,All_aug_vectors_Full)
    # print("keywords, doc, weight Full : ",keywords_docIDs_Full)

    #return dict : 
        # key : ordered ID to compare vectors with
        # val : descending order by which doc IDs (keys) are set (we used the highest weight of the query's words in that doc)
    indexed_Docs = order_docs(keywords_docIDs_IDF)
    # print("order docs for TF : ",order_docs(keywords_docIDs_TF))
    print("order docs for IDF : ",order_docs(keywords_docIDs_IDF))
    # print("order docs for Full : ",order_docs(keywords_docIDs_Full))

    
    # query vector IDF
    IDF_Query = Query_IDF_vector(documents)       # vector
    IDF_Query_dict = vector_to_dict(IDF_Query)    # dict
    print("Query Vector IDF \n")
    print((IDF_Query_dict))
    print()

    #Indexing : Get Aug IDF and Similarity only of files that are in indexed_Docs 
    print("augmented IDF vectors: \n")
    for key in indexed_Docs:
        #Get file Name
        head_tail = os.path.split(strings[key])
        file_name = head_tail[1]
        
        #Get AugIDF
        print("AugIDF of Indexed Doc ", file_name, "\n", (All_aug_vectors_IDF[key]))
        print()

        #Get Similarity
        Sim = Cosine( IDF_Query_dict , All_aug_vectors_IDF[key])
        print("Similarity via Cosine with Doc ", file_name, " : ", Sim)
        print()

        #Fill Similarity
        Similarities[file_name] = Sim
    

    #Order Similarities
    Similarities = dict( sorted(Similarities.items(), key=operator.itemgetter(1),reverse=True))
    print()
    print("Ordered Similarities")
    print(Similarities)
    