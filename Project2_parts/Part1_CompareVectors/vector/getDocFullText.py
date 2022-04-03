import xml.etree.ElementTree as ET

#returns all text over nodes
def getDocFullText(r,flag,depth,isLast,text):
    # Condition when node is None
    if r == None:
        return
       
    # Condition when the current
    # node is the root node
    if depth == 0:
        if(r.text != "" and r.text != None and r.text!=" "):
            text.append(r.text)
       
    # Condition when the node is
    # the last node of
    # the exploring depth
    elif isLast:
        if(r.text != "" and r.text != None and r.text!=" "):
            text.append(r.text)
           
        # No more childrens turn it
        # to the non-exploring depth
        flag[depth] = False
    else:
        if(r.text != "" and r.text != None and r.text!=" "):
            text.append(r.text)
        
   
    it = 0
    for i in r:  #was r.root but here r is an iterable array containing its children
        it+=1
         
        # Recursive call for the
        # children nodes
        getDocFullText(i, flag, depth + 1, it == (len(r) - 1),text)  #was r.root but here r is an iterable array containing its children
    flag[depth] = True