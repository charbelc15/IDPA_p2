from Part2.preorder import preorder
import xml.etree.ElementTree as ET
from Project1_parts.Part3.delete import delete
from Project1_parts.Part3.insert import insert
from Project1_parts.Part3.position import position
from Project1_parts.Part3.update import update

def patching(ES, tree):
    tree_preordered = preorder(tree.getroot())
    #print()
    #print("tree preorder: ",tree_preordered)
    for i in range(0, len(ES)): 
        if(ES[i][0] == "Delete:"):       
          node_pos = ES[i][1]

          #BONUS # Delete OPERATION ON TREE's PRE ORDER PATH ARRAY (next 2 lines)
          node = tree_preordered[node_pos]  #prints element with its ID
          tree_preordered.remove(node)

          #REQUIRED : ON TREE directly
          delete(tree.getroot(), node, nested=True)
          #print()
          #print("after each delete ",tree_preordered)
        
        elif( ES[i][0] == "Insert:" ):
          node_tag = ES[i][1]
          node_attributes = ES[i][2]
          node_pos_parent = ES[i][3]
          parent_node = ES[i][4]
          parent_pos_traversal = ES[i][5]

          #BONUS # INSERT OPERATION ON TREE's PRE ORDER PATH ARRAY (next 9 lines)
          # node_pos=parent_pos_traversal+1+node_pos_parent
          # if(node_pos > len(tree_preordered)):
          #   for i in range(len(tree_preordered),node_pos):  #without this for loop the function .insert will just set it at the end of the list
          #     tree_preordered.insert(i,'-')       #will be filled in later steps
          #   tree_preordered.insert(node_pos,node)
          # else:
          #   tree_preordered[node_pos] = node
          #print()
          #print("after each insert ",tree_preordered)

          #REQUIRED: ON TREE directly
          insert(tree.getroot(),node_tag,node_attributes, node_pos_parent,parent_node,parent_pos_traversal,nested=True)

        elif( ES[i][0] == "Update:" ):          
          node_del_pos = ES[i][1]
          node_del = tree_preordered[node_del_pos]
          node_ins_pos = ES[i][2]
          node_ins = ES[i][3]

          #BONUS # Update OPERATION ON TREE's PRE ORDER PATH ARRAY (next 3 lines)
          tree_preordered[node_del_pos] = node_ins  #both nodes (to insert and delete have the same index #Chawathe condition) + only need val of inserted node
          #print()
          #print("after each update ",tree_preordered)

          #REQUIRED ON TREE directly
          update(tree.getroot(), node_del, node_ins, nested=True)
    tree_preordered = preorder(tree.getroot())
    print()
    print("output's pre order traversal : ",tree_preordered)