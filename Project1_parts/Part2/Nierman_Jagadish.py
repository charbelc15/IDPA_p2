import xml.etree.ElementTree as ET
from Project1_parts.Part2.CostInsTree import CostInsTree
from Project1_parts.Part2.CostDelTree import CostDelTree
from Project1_parts.Part2.getSubTree import getSubTree
import numpy as np

global dist

def TED(tree1, tree2):
                                                                                     
                                                                                     # 1) M and N
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    Nb_children1=0
    Nb_children2=0

    #1st level Children tree list of A (only need 1st cause this is recursive)
    for child in root1:
        Nb_children1+=1

    #1st level Children tree list of B (only need 1st cause this is recursive)
    for child in root2:
        Nb_children2+=1

    M=Nb_children1
    N=Nb_children2

    #print(M)
    #print(N)

                                                                                    # 2) dist

                                                                                    #empty 2D dist matrix

    nb_rows = int(M+1)         #R(A) + M children 
    nb_cols = int(N+1)      #R(B) + N children

    dist = [[0 for x in range(nb_cols)] for y in range(nb_rows)]  #global 

                                                                                        # 3) dist[0][0]

    if(root1.tag==root2.tag):
        dist[0][0]=0
    else:
        dist[0][0]=1

                                                                                        # 4) first row - first column

    A = getSubTree(tree1) #1st level Children tree list of A (only need 1st cause this is recursive)
    for i in range(1, M+1): # M+1 excluded
        treeA=ET.ElementTree()
        treeA._setroot(A[i-1])  #SUBTREE A1 here is at position 0 of the children's trees list
        dist[i][0]=dist[i-1][0] + CostDelTree(treeA, tree2)  # Cost of deletingAi (going down)



    B = getSubTree(tree2) #1st level Children tree list of B (only need 1st cause this is recursive)
    for j in range(1, N+1): # N+1 excluded
        treeB=ET.ElementTree()
        treeB._setroot(B[j-1])
        dist[0][j]=dist[0][j-1] + CostInsTree(tree1, treeB) # Cost of Inserting Bi (going right)


                                                                                            # 5) Rest of Matrix
    
    for i in range(1, M+1): #M+1 excluded
        treeA=ET.ElementTree()
        treeA._setroot(A[i-1])
        for j in range(1, N+1): #N+1 excluded
            treeB=ET.ElementTree()
            treeB._setroot(B[j-1])
            dist[i][j]= min(
                dist[i-1][j-1] + TED(treeA, treeB),
                dist[i-1][j] + CostDelTree(treeA, tree2),
                dist[i][j-1] + CostInsTree(tree1, treeB)
            )
    #just a method for display purposes
    matrix = np.array(dist)
    #print(matrix)
    return dist[M][N]