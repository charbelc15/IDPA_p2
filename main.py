
import xml.etree.ElementTree as ET

from numpy import full
from Project1_parts.Part2.Nierman_Jagadish import TED
from Project1_parts.Part1.displayTree import displayTree
from Project1_parts.Part2_Chawathe.Chawathe import Chawathe
from Project1_parts.Part2_Chawathe.getNodesHeights import getNodesHeights
from Project2_parts.Part1_CompareVectors.term_weighting.IDF import IDF
from Project2_parts.Part1_CompareVectors.term_weighting.TF import TF
from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray

from Project2_parts.Part1_CompareVectors.term_weighting.weight import weight
from Project2_parts.Part1_CompareVectors.term_weighting.weight_TF import weight_TF
from Project2_parts.Part1_CompareVectors.term_weighting.weight_IDF import weight_IDF
from Project2_parts.Part1_CompareVectors.vector.vector_Full import vector_Full
from Project2_parts.Part1_CompareVectors.vector.vector_IDF import vector_IDF
from Project2_parts.Part1_CompareVectors.vector.vector_TF import vector_TF


string1='xml_files/test5.xml'
string2='xml_files/test6.xml' 


                                                                                                        #Part 1.1 XML TO TREE MODEL
#input:xml files      output: trees
tree1 = ET.parse(string1) #this gets the file into a tree structure
tree2 = ET.parse(string2)

tree_root1 = tree1.getroot() #this gives us the root element of the file
tree_root2 = tree2.getroot() #this gives us the root element of the file

                                                                                                         #Part 1.2 Display tree
flagcounter = 0
for i in tree_root1.iter():
    flagcounter+=1

flag = [False]*flagcounter
displayTree(tree_root1,flag,0,False)


                                                                                                            #PART 2.1 Similarity

flagcounter1 = 0
for i in tree_root1.iter(): 
    flagcounter1+=1

LD_pairA=[]
flag1 = [False]*flagcounter1
getNodesHeights(tree_root1,flag1,0,False,LD_pairA) 
print()
print("LD-pair A: ", LD_pairA)

flagcounter2 = 0
for i in tree_root2.iter():
    flagcounter2+=1

LD_pairB=[]
flag2 = [False]*flagcounter2
getNodesHeights(tree_root2,flag2,0,False,LD_pairB) 
print()
print("LD-pair B: ",LD_pairB)


#Note: chawathe returns at 
# pos 0 : cost matrix for ES(A,B)   
# at pos1: ED(A,B) value (dist[M][N])
val = Chawathe(LD_pairA, LD_pairB)[1]
print()
print("distance ", val)
Similarity = 1/(val+1)
print()
print("Similarity according to Chawathe",Similarity)


#nierman
val = TED(tree1, tree2)
print()
print("distance ", val )
Similarity = 1/(val+1)
print()
print("Similarity according to Nierman",Similarity)







                                                                                                #PART 4      TREE TO XML


#return 2 output trees to the 2 xml files

newXML1 = ET.tostring(tree1.getroot(), encoding='utf8').decode('utf8')
text_file1 = open("new_Test1.xml", "w")
n1 = text_file1.write(newXML1)
text_file1.close()


newXML2 = ET.tostring(tree2.getroot(), encoding='utf8').decode('utf8')
text_file2 = open("new_Test2.xml", "w")
n2 = text_file2.write(newXML2)
text_file2.close()



#Project 2 testing
word = "it"
word = word.lower()
doc = 0
documents=["My Name Is Charbel? Yes it is Charbel", "Is my name Charbel?", "No I dont think so"]
#documents=["My Name Is Charbel? Yes it is Charbel"]
print(countsArray(documents)[0])
print(countsArray(documents)[1])

print("TF: " , TF(word, countsArray(documents)[0], countsArray(documents)[1],doc))
print("IDF: " , IDF(word, countsArray(documents)[0], countsArray(documents)[1]))
print("Full weight: " , weight(word,doc,documents))
print("Weight with TF only: " , weight_TF(word,doc,documents))
print("Weight with IDF only: " , weight_IDF(word,doc,documents))

docs = ["My Name Is Charbel? Yes it is Charbel", "ECE"]

# TF    ||      IDF         ||      BOTH    
# FOR     DOC1 of docs!!!!!! **
# !!! vector TF ONLY RETURNS first array of counter_Arrays




# words positions
print(vector_TF(docs)[0])
# TF array !!SYNTAX!! [[ ]]
test_vector_TF = vector_TF(docs)[1][0]
print(test_vector_TF)
#correct : at position 0 values are x2

# words positions
print(vector_IDF(docs)[0])
# TF array !!SYNTAX!! [[ ]]
test_vector_IDF = vector_IDF(docs)[1]
print(test_vector_IDF)
#correct : all values are the same      since each unique word is contained in only 1 document ln(2/1)

#method 1 for Full : using weight.py (just like augmented_vector_IDF)
# # words positions
# print(augmented_vector_Full(doc1)[0])
# # TF array !!SYNTAX!! [[ ]]
# print(augmented_vector_Full(doc1)[1])


#method 2 for Full : using the produced IDF and TR vectors : mulitply elements that are at same position (1 from each vector)
test_vector_Full = vector_Full(test_vector_TF, test_vector_IDF)
print(test_vector_Full)
#correct : at position 0 and at 2 values are x2 (charbel \\ is)
#correct : at position 1 we have a 0 : ECE is not in document 1


