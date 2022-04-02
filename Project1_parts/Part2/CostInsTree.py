from logging import root
import xml.etree.ElementTree as ET
from Project1_parts.Part2.sameTree import sameTree
from Project1_parts.Part2.subTree import subTree

#cost of inserting tree B(i)
def CostInsTree(treeA, treeB):

    Nb_children=0

    rootA = treeA.getroot()
    rootB = treeB.getroot()
        

    if(subTree(rootA,rootB)): #CHECK if !!!! B !!!! is subtree of !!!! A !!!!
        return 1
    else:
        root=treeB.getroot()
        for child in root.iter():
            Nb_children+=1
        return(Nb_children)
        


