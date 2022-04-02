import xml.etree.ElementTree as ET
# ------------------Charbel-------------------- 
# Printing
# identifies Text Values + checks if they are empty (to not display them) 
# identfies Empty and Non Empty Attributes (returned in a dictionnary; r.attrib), to check if empty : bool(r.attrib)
# Orders attributes by alph. order of keys


# Process

# (depth) Initialize a variable to store the current depth of the node, for the root node the depth is 0. 
# (flag) Declare a boolean array to store the current exploring depths and initially mark all of them to False.
# (line 34) If the current node is a root node that is the depth of the node is 0, then simply print the data of the node.
# Otherwise, Iterate over a loop from 1 to the current depth of node and print, ‘|’ and three spaces for each of the exploring depth and for non-exploring depth print three spaces only.
# Print the current value of the node and move the output pointer to the next line.
# If the current node is the last node of that depth then mark that depth as non-exploring.
# Similarly, explore all the child nodes with the recursive call.

def displayTree(r,flag,depth,isLast):
    # Condition when node is None
    if r == None:
        return
       
    # Loop to print the depths of the
    # current node
    for i in range(1, depth):
        # Condition when the depth
        # is exploring
        if flag[i]:
            print("| ","", "", "", end = "")
           
        # Otherwise print
        # the blank spaces
        else:
            print(" ", "", "", "", end = "")
       
    # Condition when the current
    # node is the root node
    if depth == 0:
        print("+---", r.tag)
        if(r.text != "" and r.text != None and r.text!=" "):
            print("              +tag: ", r.text)
        if(bool(r.attrib)):
            attributesString=""
            for i in sorted(r.attrib):
                attributesString+=" K: "+ i+ " V: "+ r.attrib.get(i)
            print("                         +Attributes: ", attributesString)
       
    # Condition when the node is
    # the last node of
    # the exploring depth
    elif isLast:
        print("     +---", r.tag)
        if(r.text != "" and r.text != None and r.text!=" "):
            print("              +tag: ", r.text)
        if(bool(r.attrib)):
            attributesString=""
            for i in sorted(r.attrib):
                attributesString+=" K: "+ i+ " V: "+ r.attrib.get(i)
            print("                         +Attributes: ", attributesString)
           
        # No more childrens turn it
        # to the non-exploring depth
        flag[depth] = False
    else:
        print("     +---", r.tag)
        if(r.text != "" and r.text != None and r.text!=" "):
            print("              +tag: ", r.text)
        if(bool(r.attrib)):
            attributesString=""
            for i in sorted(r.attrib):
                attributesString+=" K: "+ i+ " V: "+ r.attrib.get(i)
            print("                         +Attributes: ", attributesString)
        
   
    it = 0
    for i in r:  #was r.root but here r is an iterable array containing its children
        it+=1
         
        # Recursive call for the
        # children nodes
        displayTree(i, flag, depth + 1, it == (len(r) - 1))  #was r.root but here r is an iterable array containing its children
    flag[depth] = True