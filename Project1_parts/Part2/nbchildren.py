import xml.etree.ElementTree as ET

# tree1 = ET.parse('xml_files/test1.xml') #this gets the file into a tree structure
# tree2 = ET.parse('xml_files/test1.xml')


# Gives total number of elements/subtrees: try it out in xml2tree.py
#   M=nbchildren(tree1)
#   N=nbchildren(tree2)


def nbchildren(tree):

    root = tree.getroot()
    Nb_children=0

    for child in root.iter():
        Nb_children+=1

    return Nb_children