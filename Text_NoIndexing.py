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

#1. Augmented Vectors
    #1.1 Element Properties of each doc
counter = 1
strings=[
    'xml_files/Project2_test1.xml' # 1
   ,'xml_files/Project2_test2.xml' # 2
#    ,'xml_files/Project2_test3.xml' # 3
#    ,'xml_files/Project2_test4.xml' # 4
#    ,'xml_files/Project2_test5.xml' # 5
#    ,'xml_files/Project2_test6.xml' # 6
#    ,'xml_files/Project2_test7.xml' # 7
#    ,'xml_files/Project2_test8.xml' # 8
#    ,'xml_files/Project2_test9.xml' # 9
#    ,'xml_files/Project2_test10.xml'  # 10

    
]
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
All_aug_vectors_TF=[]
All_aug_vectors_IDF=[]
All_aug_vectors_Full=[]




















Query = "tannir ece"
documents.append(Query)

























for i in range(len(All_Filtered_Texts)):

    # Get parameters for functions
    ElementProperties = All_ElementProperties[counter]
    Filtered_Text = All_Filtered_Texts[counter]

    # Get TF aug vector of each doc
    aug_vector_TF_1 = augmented_vector_TF(documents,ElementProperties,counter,Filtered_Text)

    # Get IDF aug vector of each doc
    aug_vector_IDF_1 = augmented_vector_IDF(documents,ElementProperties,counter,Filtered_Text)

    # Get Full aug vector of each doc
    _vector_TF_1 = vector_TF(documents)[1]
    _vector_IDF_1 = vector_IDF(documents)[1]
    aug_vector_Full_1 = augmented_vector_Full(documents,ElementProperties,counter,Filtered_Text,_vector_TF_1,_vector_IDF_1)

    # Get Dictionary of each aug vector
    TF_dict1 = vector_to_dict(aug_vector_TF_1)
    IDF_dict1 = vector_to_dict(aug_vector_IDF_1)
    Full_dict1 = vector_to_dict(aug_vector_Full_1)

    # Append Dictionaries aug vector of each doc
    All_aug_vectors_TF.append(TF_dict1)
    All_aug_vectors_IDF.append(IDF_dict1)
    All_aug_vectors_Full.append(Full_dict1)

    # UPDATE COUNTER AT END OF LOOP
    counter+=1 #!!!!!!!!!!!!!!!
    


# aug_vector_TF_1 = augmented_vector_TF(documents,ElementProperties,0,Filtered_Text)
# aug_vector_TF_2 = augmented_vector_TF(documents,ElementProperties,1,Filtered_Text)
# aug_vector_TF_3 = augmented_vector_TF(documents,ElementProperties,2,Filtered_Text)
# aug_vector_TF_4 = augmented_vector_TF(documents,ElementProperties,3,Filtered_Text)

# aug_vector_IDF_1 = augmented_vector_IDF(documents,ElementProperties,0,Filtered_Text)
# aug_vector_IDF_2 = augmented_vector_IDF(documents,ElementProperties,1,Filtered_Text)
# aug_vector_IDF_3 = augmented_vector_IDF(documents,ElementProperties,2,Filtered_Text)
# aug_vector_IDF_4 = augmented_vector_IDF(documents,ElementProperties,3,Filtered_Text)

# _vector_TF_1 = vector_TF(documents)[1]
# _vector_IDF_1 = vector_IDF(documents)[1]
# _vector_TF_2 = vector_TF(documents)[1]
# _vector_IDF_2 = vector_IDF(documents)[1]
# _vector_TF_3 = vector_TF(documents)[1]
# _vector_IDF_3 = vector_IDF(documents)[1]
# _vector_TF_4 = vector_TF(documents)[1]
# _vector_IDF_4 = vector_IDF(documents)[1]

# aug_vector_Full_1 = augmented_vector_Full(documents,ElementProperties,0,Filtered_Text,_vector_TF_1,_vector_IDF_1)
# aug_vector_Full_2 = augmented_vector_Full(documents,ElementProperties,1,Filtered_Text,_vector_TF_2,_vector_IDF_2)
# aug_vector_Full_3 = augmented_vector_Full(documents,ElementProperties,2,Filtered_Text,_vector_TF_3,_vector_IDF_3)
# aug_vector_Full_4 = augmented_vector_Full(documents,ElementProperties,3,Filtered_Text,_vector_TF_4,_vector_IDF_4)



# #Augmented vector To dictionaries
# #  add the values for the same elements

# TF_dict1 = vector_to_dict(aug_vector_TF_1)
# TF_dict2 = vector_to_dict(aug_vector_TF_2)
# TF_dict3 = vector_to_dict(aug_vector_TF_3)
# TF_dict4 = vector_to_dict(aug_vector_TF_4)

# IDF_dict1 = vector_to_dict(aug_vector_IDF_1)
# IDF_dict2 = vector_to_dict(aug_vector_IDF_2)
# IDF_dict3 = vector_to_dict(aug_vector_IDF_3)
# IDF_dict4 = vector_to_dict(aug_vector_IDF_4)

# Full_dict1 = vector_to_dict(aug_vector_Full_1)
# Full_dict2 = vector_to_dict(aug_vector_Full_2)
# Full_dict3 = vector_to_dict(aug_vector_Full_3)
# Full_dict4 = vector_to_dict(aug_vector_Full_4)


print()
print("augmented TF vectors: ")

print("AugTF Doc1 ", (All_aug_vectors_TF[0]))
# print("len2", (All_aug_vectors_TF[1]))
# print("len2", (All_aug_vectors_TF[2]))
# print("len2", (All_aug_vectors_TF[3]))
# print("len1", (All_aug_vectors_TF[4]))
# print("len2", (All_aug_vectors_TF[5]))
# print("len2", (All_aug_vectors_TF[6]))
# print("len2", (All_aug_vectors_TF[7]))
# print("len2", (All_aug_vectors_TF[8]))
# print("len2", (All_aug_vectors_TF[9]))

print()
print("augmented IDF vectors: ")

print()
print("AugIDF of Doc1 ", All_aug_vectors_IDF[0])
# print("len2", (All_aug_vectors_IDF[1]))
# print("len2", (All_aug_vectors_IDF[2]))
# print("len2", (All_aug_vectors_IDF[3]))
# print("len2", (All_aug_vectors_IDF[4]))
# print("len2", (All_aug_vectors_IDF[5]))
# print("len2", (All_aug_vectors_IDF[6]))
# print("len2", (All_aug_vectors_IDF[7]))
# print("len2", (All_aug_vectors_IDF[8]))
# print("len2", (All_aug_vectors_IDF[9]))

print()
print("AugFull of Doc1 ", All_aug_vectors_Full[0])
# print("len2", All_aug_vectors_Full[1])
# print("len2", All_aug_vectors_Full[2])
# print("len2", All_aug_vectors_Full[3])
# print("len2", All_aug_vectors_Full[4])
# print("len2", All_aug_vectors_Full[5])
# print("len2", All_aug_vectors_Full[6])
# print("len2", All_aug_vectors_Full[7])
# print("len2", All_aug_vectors_Full[8])
# print("len2", All_aug_vectors_Full[9])


print()

print("Similarity via PCC: ", PCC( All_aug_vectors_TF[0] , All_aug_vectors_TF[1] ) )
print("Similarity via Cosine: ", Cosine( All_aug_vectors_TF[0] , All_aug_vectors_TF[1] ) )

#Indexing
text_to_search_for=Query
    #remove special characters, I, a
filtered_text_to_search_for = Filter_Text(text_to_search_for)
    #remove leading / trailing whitespaces
filtered_text_to_search_for = filtered_text_to_search_for.strip()
    #split the words
Keywords = split_query(filtered_text_to_search_for)

# remove query from repository to search from
QueryDocs=[]
for doc in documents:
    QueryDocs.append(doc)
QueryDocs.remove(Query)

#return dict : 
    # keys: (String) keyword 
    # values : (dictionary) docIDs where keyword is , weight of the word at that doc
keywords_docIDs_TF = index_Query_TF(Keywords,QueryDocs,All_aug_vectors_TF)
print("keywords, doc, weight TF : ",keywords_docIDs_TF)

keywords_docIDs_IDF = index_Query_TF(Keywords,QueryDocs,All_aug_vectors_IDF)
print("keywords, doc, weight IDF : ",keywords_docIDs_IDF)

keywords_docIDs_Full = index_Query_Full(Keywords,QueryDocs,All_aug_vectors_Full)
print("keywords, doc, weight Full : ",keywords_docIDs_Full)

#return dict : 
    # key : ordered ID to compare vectors with
    # val : descending order by which doc IDs (keys) are set (we used the highest weight of the query's words in that doc)
print("order docs for TF : ",order_docs(keywords_docIDs_TF))
print("order docs for IDF : ",order_docs(keywords_docIDs_IDF))
print("order docs for Full : ",order_docs(keywords_docIDs_Full))

print(Keywords)
print(QueryDocs)

print(documents)

# query TF
TF_Query = Query_TF_vector(documents)       # vector
TF_Query_dict = vector_to_dict(TF_Query)    # dict
print()
print((TF_Query_dict))

# query IDF
IDF_Query = Query_IDF_vector(documents)     # vector
IDF_Query_dict = vector_to_dict(IDF_Query)  # dict
print()
print((IDF_Query_dict))

#query Full
Q_vector_TF_1 = vector_TF(documents)[1]
Q_vector_IDF_1 = vector_IDF(documents)[1]
Full_Query = Query_Full_vector(documents, Q_vector_TF_1, Q_vector_IDF_1)  # vector
Full_Query_dict = vector_to_dict(Full_Query)
print()
print((Full_Query_dict))

# print(filtered_text_to_search_for)
# print(len(filtered_text_to_search_for))
# docID = index_docID(documents,filtered_text_to_search_for)
# print("examplary is in DocID: ", docID)
