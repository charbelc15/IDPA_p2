import xml.etree.ElementTree as ET
def getNodesHeights(r,flag,depth,isLast,heights):
    # Condition when node is None
    if r == None:
        return

    #       TURNED OFF dont want to print    
       
    # # Loop to print the depths of the
    # # current node
    # for i in range(1, depth):
    #     # Condition when the depth
    #     # is exploring
    #     if flag[i]:
    #         print("| ","", "", "", end = "")
           
    #     # Otherwise print
    #     # the blank spaces
    #     else:
    #         print(" ", "", "", "", end = "")
       
    # Condition when the current
    # node is the root node
    if depth == 0:
        heights.append([r.tag+"",depth])
       
    # Condition when the node is
    # the last node of
    # the exploring depth
    elif isLast:
        heights.append([r.tag+"",depth])
           
        # No more childrens turn it
        # to the non-exploring depth
        flag[depth] = False
    else:
        heights.append([r.tag+"",depth])
        
   
    it = 0
    for i in r:  #was r.root but here r is an iterable array containing its children
        it+=1
         
        # Recursive call for the
        # children nodes
        getNodesHeights(i, flag, depth + 1, it == (len(r) - 1),heights)  #was r.root but here r is an iterable array containing its children
    flag[depth] = True