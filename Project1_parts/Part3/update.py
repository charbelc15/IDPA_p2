
def update(root, node_del, node_ins, nested=False):
    if(root==node_del):
        #update node_del to node_ins
        root.tag = node_ins.tag
        if(node_ins.text != None and node_ins.attrib != None):
            root.text = node_ins.text
            for x in range(0,len(root.attrib)):   #Delete all attributes from first tree
                del root.attrib[ root.attrib.keys()[0]]
            for i in range(0, len(node_ins.attrib)): #Add all other attributes from other tree
                root.set(node_ins.attrib.keys()[i],node_ins.values()[i])

        
    for child in reversed(root):
        if nested:
            if len(child) >= 1:
                update(child,node_del, node_ins)
        if child==node_del:
            #update node_del to node_ins
            child.tag = node_ins.tag
            if(node_ins.text != None and node_ins.attrib != None):
                child.text = node_ins.text
                for x in range(0,len(child.attrib)):   #Delete all attributes from first tree
                    del child.attrib[ child.attrib.keys()[0]]
                for i in range(0, len(node_ins.attrib)): #Add all other attributes from other tree
                    child.set(node_ins.attrib.keys()[i],node_ins.values()[i])
                