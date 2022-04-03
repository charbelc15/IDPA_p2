import xml.etree.ElementTree as ET

#returns factor of path 
def getPathFactor(r,flag,depth,isLast,factors):
    # Condition when node is None
    if r == None:
        return
       
    # Condition when the current
    # node is the root node
    if depth == 0:
        factors.append([r, r.tag+"",1/(1+depth), r.text.split('\n')[0]])
       
    # Condition when the node is
    # the last node of
    # the exploring depth
    elif isLast:
        factors.append([r, r.tag+"",1/(1+depth), r.text.split('\n')[0]])
           
        # No more childrens turn it
        # to the non-exploring depth
        flag[depth] = False
    else:
        factors.append([r, r.tag+"",1/(1+depth), r.text.split('\n')[0]])
        
   
    it = 0
    for i in r:  #was r.root but here r is an iterable array containing its children
        it+=1
         
        # Recursive call for the
        # children nodes
        getPathFactor(i, flag, depth + 1, it == (len(r) - 1),factors)  #was r.root but here r is an iterable array containing its children
    flag[depth] = True