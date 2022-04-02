
from Project1_parts.Part2.preorder import preorder
from Project1_parts.Part3.position import position
from lxml import etree as et


def insert(root, node_tag, node_attrib , node_pos_parent,    parent_node,  parent_pos_traversal   , nested=False):
    
    if(root.tag==parent_node and parent_pos_traversal==0):
        y = et.SubElement(root, node_tag)
        attribs = dict(node_attrib)
        for key in attribs:
            y.attrib[key] = attribs[key]
        root.insert(node_pos_parent, y)
        if nested:
            if len(root) > 1:
                insert(root, node_tag, node_attrib, node_pos_parent, parent_node, parent_pos_traversal)
        #insert(root, node_tag, node_attrib, node_pos_parent, parent_node, parent_pos_traversal)     
        #root is my parent --> insert the node as a subelement
    for child in reversed(root):
        child_pos_traversal=position(root,child)
        if nested:
            if len(child) >= 1:
                insert(child, node_tag, node_attrib, node_pos_parent, parent_node, parent_pos_traversal)
        if (child.tag ==parent_node and (child_pos_traversal==parent_pos_traversal)):  
            y = et.SubElement(child, node_tag)
            attribs = dict(node_attrib)
            for key in attribs:
                y.attrib[key] = attribs[key] 
            child.insert(node_pos_parent, y)

