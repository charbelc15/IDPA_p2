from logging import root
import xml.etree.ElementTree as ET
from Project1_parts.Part2.preorder import preorder
from Project1_parts.Part2.sameTree import sameTree

# !!!!!!!!!!!!!!! IN THAT ORDER !!!!!!!!!!!!!!!!! checking if     root2        is subtree of      root1
def subTree(root1, root2) -> bool:
    
    #STEP 1 and 2
    # 1) if tree2 is empty : it is a subtree of tree1
    if root2 is None: return True
    
    # 2) we already checked that tree2 is not empty,    but if tree1 is empty and tree2 is not empty            then     tree2 is not part of tree1 
    if root1 is None: return False



    #STEP 3 and 4
    # 3) if, from this point/root, they are the same tree       return true
    if sameTree(root1,root2): return True

    # 4) but if they are NOT the same tree, then keep digging : 
    
    for child_d1 in root1.iter():
        for child_d2 in root2:
            return subTree(child_d1,child_d2)

    
    # list = preorder(root2)
    # for child_d1 in root1.iter():
    #     for child_d2 in list:
    #         return subTree(child_d1,child_d2)
       