import numpy as np

from Project1_parts.Part2.preorder import preorder
from Project1_parts.Part3.position import position


              
def backtrace(tree1, tree2, first, second, matrix):
    f = [x for x in first]
    s = [x for x in second]
    new_f, new_s = [], []
    row = len(f)
    col = len(s)
    trace = [[row, col]]
    steps=[]

    while True:
        if f[row - 1] == s[col - 1]:
            cost = 0
        else:
            cost = 1 

        r = matrix[row][col]
        a = matrix[row - 1][col]
        b = matrix[row - 1][col - 1]
        c = matrix[row][col - 1]

        if b == min(a,b,c):
            # when diagonal backtrace substitution or no substitution
            if(cost != 0):
                node_to_insert=preorder(tree2.getroot())[col-1] 
                steps.append(["Update:", row-1, col-1, node_to_insert])
            trace.append([row - 1, col - 1])
            new_f = [f[row - 1]] + new_f
            new_s = [s[col - 1]] + new_s
            row, col = row - 1, col - 1

        else:
            # deletion
            if a == min(a,b,c):
                steps.append(["Delete:", row-1])   
                trace.append([row - 1, col])
                #new_f = ["-"] + new_f #deleting node of first tree A (Del(Ai)) from first tree A
                new_s = [f[row - 1]] + new_s
                row, col = row - 1, col
            # insertion
            elif c == min(a,b,c):
                node_to_insert=preorder(tree2.getroot())[col-1] #gets the ACTUAL ELEMENT
                node_to_insert_position_acc_parent = node_to_insert.getparent().index(node_to_insert)
                node_to_insert_position_acc_traversal = col -1
                parent_pos_acc_traversal = position(tree2.getroot(), node_to_insert.getparent())

                node_tag=node_to_insert.tag
                node_attributes=node_to_insert.attrib
                
                print("here" , node_attributes)

                steps.append(["Insert:" , node_tag, node_attributes, node_to_insert_position_acc_parent, node_to_insert.getparent().tag, parent_pos_acc_traversal]) 
                trace.append([row, col - 1])
                new_f = [s[col - 1]] + new_f 
                new_s = [s[col - 1]] + new_s
                row, col = row, col - 1

        # Exit the loop
        if row == 0 or col == 0:
            return trace, steps, new_f, new_s
 
