from logging import root
import xml.etree.ElementTree as ET

from Project1_parts.Part2.preorder import preorder


def sameTree(root1, root2) -> bool:    

    Subtree1 = preorder(root1)
    Subtree2 = preorder(root2)

    list=[]

    #now , both root1 and root2 and not empty       AND         root1 same as root2
    if(len(Subtree1)!=len(Subtree2)):    #different number of elements --> Not same
        return False
    else:
        for i in range(0, len(Subtree1)-1): #checking if order of all elements is same
            if(Subtree1[i].tag == Subtree2[i].tag):
                list.append("true")

        if(len(list)==0):  #if we dont have any result --> no "true" values --> exit
            return False 

        for answer in list:
            if(answer != "true"): #if one of them is not same as other according to parallel positions --> not same
                return False
        
        return True #if we looped over all the list and theres no false answer --> all are true --> return True