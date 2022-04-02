from logging import root
import xml.etree.ElementTree as ET
from Project1_parts.Part2.preorder import preorder
from Project1_parts.Part2.sameTree import sameTree

# !!!!!!!!!!!!!!! IN THAT ORDER !!!!!!!!!!!!!!!!! checking if     root2        is subtree of      root1
def subTree(root1, root2) -> bool:
 
    list=[]
    Subtrees=preorder(root1)
    #print(Subtrees)
    for subtree in Subtrees: #go through all subtrees
        if sameTree(root2,subtree): #if one of them is same as ours (root2), return True
            list.append("true")

    for answer in list:
        if(answer == "true"): #if one of them is subtree --> We have located a subtree -> True
            return True

    return False   #if we looped through them all and none is same as ours(root2), return False