
import xml.etree.ElementTree as ET
from Project1_parts.Part2.Nierman_Jagadish import TED
from Project1_parts.Part1.displayTree import displayTree
from Project1_parts.Part2_Chawathe.Chawathe import Chawathe
from Project1_parts.Part2_Chawathe.getNodesHeights import getNodesHeights


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