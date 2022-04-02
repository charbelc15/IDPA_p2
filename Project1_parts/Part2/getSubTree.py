import xml.etree.ElementTree as ET

from Project1_parts.Part2.preorder import preorder

def getSubTree(treeA):
    # return inner subtrees (each as a list) in an array of *tree lists*
    # treeA is our parameter
    # trees[] contains the full subtrees lists (represented by node Element, each element can have its children accessed also)
    
    trees = []
    treeA_root = treeA.getroot()

    # Looping through all nodes of treeA
    for child in treeA_root:
        trees.append(child)

    return trees

