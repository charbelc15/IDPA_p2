import xml.etree.ElementTree as ET

#tree: A tree containing trees
def inv_preorder(preorder):
    tree = ET.ElementTree

    if preorder[0] is None:
        return 

    tree._setroot(preorder[0])

    for x in preorder:
        tree._setroot(inv_preorder(x))        
    
    return tree 
