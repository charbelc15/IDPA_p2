from Project1_parts.Part2_Chawathe.Delete import Delete
from Project1_parts.Part2_Chawathe.Insert import Insert
from Project1_parts.Part2_Chawathe.Update import Update
import numpy as np


def Chawathe(LD_pairA, LD_pairB):
                                                                                     
                                                                                     # 1) |A*| and |B*|
    LD_pairA_size=len(LD_pairA)
    LD_pairB_size=len(LD_pairB)

                                                                                    # 2) dist

                                                                                    #empty 2D dist matrix

    nb_rows = int(LD_pairA_size+1)         # . + LD_pairA elements 
    nb_cols = int(LD_pairB_size+1)      # . + LD_pairB elements

    dist = [[0 for x in range(nb_cols)] for y in range(nb_rows)]  #global 

                                                                                        # 3) dist[0][0]

    dist[0][0]=0

                                                                                        # 4) first row - first column

    for i in range(1, LD_pairA_size+1): # LD_pair_size+1 value excluded
        dist[i][0]=dist[i-1][0]+1  # Cost of deleting Ai (going down)


    for j in range(1, LD_pairB_size+1): # LD_pair_size+1 excluded
        dist[0][j]=dist[0][j-1] + 1 # Cost of Inserting Bi (going right)

                                                                                        # 5) Conditions
    # Created Methods
    # Condition 1 : canUpdate
    # Condition 2 : canDelete
    # Condition 3 : canInsert
                                                                                    
                                                                                        # 6) Rest of Matrix
    
    for i in range(1, LD_pairA_size+1):
        for j in range(1, LD_pairB_size+1):
            dist[i][j]= min(
                                            #depth #pos1      #tag #pos0             #depth #pos1            #tag #pos0
                dist[i-1][j-1] + Update(LD_pairA[i-1][1]  ,  LD_pairA[i-1][0]  , LD_pairB[j-1][1]  ,  LD_pairB[j-1][0]  ),
                dist[i-1][j] + Delete(  LD_pairA[i-1][1]  ,  LD_pairB[j-1][1]  ,  j  ,  LD_pairB_size  ),
                dist[i][j-1] + Insert(  LD_pairA[i-1][1]  ,  LD_pairB[j-1][1]  ,  i  ,  LD_pairA_size  ) #j is ahead of us by 1 (starts at index 1 since we have dist[0][0])   AND  list index starts at 0
            )
    #just a method for display purposes
    matrix = np.array(dist)
    #print(matrix)
    return [matrix, dist[LD_pairA_size][LD_pairB_size]]