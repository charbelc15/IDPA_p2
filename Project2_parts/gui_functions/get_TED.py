
import os
from Project1_parts.Part2.Nierman_Jagadish import TED
import xml.etree.ElementTree as ET
import operator

def getTED(FilePath):

    tree_ref = ET.parse(FilePath)

    strings=[
    'xml_files/Project2_N_test1.xml' # 1
   ,'xml_files/Project2_N_test2.xml' # 2
   ,'xml_files/Project2_N_test3.xml' # 3
   ,'xml_files/Project2_N_test4.xml' # 4
   ,'xml_files/Project2_N_test5.xml' # 5
   ,'xml_files/Project2_N_test6.xml' # 6
   ,'xml_files/Project2_N_test7.xml' # 7
   ,'xml_files/Project2_N_test8.xml' # 8
#    ,'xml_files/Project2_test9.xml' # 9
#    ,'xml_files/Project2_test10.xml'  # 10
    ]

    Similarities={}

    for string in strings:

        tree = ET.parse(string)
        val = TED(tree_ref , tree)
        print()
        print("distance ", val )
        Similarity = 1/(val+1)
        print()
        print("Similarity according to Nierman",Similarity)

        #Get File name
        head_tail = os.path.split(string)
        file_name = head_tail[1]
        print("Tail of '% s:'" % string, head_tail[1] , "\n")
        
        #Key: File Name
        #Value : Similarity
        Similarities[file_name] = Similarity

    #Order similarities
    Similarities = dict( sorted(Similarities.items(), key=operator.itemgetter(1),reverse=True))
    print(Similarities)

