from statistics import mean

import numpy as np

def PCC(dictA,dictB):
    values_A=[]
    values_B=[]
    
    #Extracting values from dictionaries
    for element in dictA:
        valueA = element[1]
        values_A.append(valueA)
    
    for element in dictB:
        valueB = element[1]
        values_B.append(valueB)

    average_A = mean(values_A)
    average_B = mean(values_B)

    #Getting nominator
    nominator = 0
    for i in range(0,len(values_A)):
        Ai_minus_Abar = (values_A[i]-average_A)
        Bi_minus_Bbar = (values_B[i]-average_B)
        nominator += Ai_minus_Abar*Bi_minus_Bbar

    #Getting denominator

    Ai_minus_Abar_squared = 0
    for i in range(0,len(values_A)):
        Ai_minus_Abar_squared += np.power( (values_A[i]-average_A) ,2)
        
    Bi_minus_Bbar_squared = 0
    for i in range(0,len(values_B)):
        Bi_minus_Bbar_squared += np.power( (values_B[i]-average_B) ,2)

    product = Ai_minus_Abar_squared * Bi_minus_Bbar_squared

    denominator = np.power( product , 0.5 )

    #get Similarity

    

    #!! if all terms are of 0 factor --> denominator will be 0 --> return a 0 similarity value
    if denominator==0:
        return 0
    Sim = np.divide(nominator,denominator)

    return Sim


# if __name__ == "__main__":
#     values_A = [['liu', 0.6931471805599453], ['charbel', 0.0], ['aub', 0.6931471805599453], ['ece', 0.23104906018664842], ['john', 0.17328679513998632], ['cramer', 0.17328679513998632], ['john', 0.17328679513998632], 
# ['takagi', 0.17328679513998632], ['mark', 0.17328679513998632], ['cramer', 0.17328679513998632]]
#     values_B =[['liu', 0], ['charbel', 1.0], ['aub', 1.0], ['ece', 0.3333333333333333], ['john', 0.25], ['cramer', 0.25], ['john', 0.25], ['takagi', 0.25], ['mark', 0.25], ['cramer', 0.25]]
#     print(PCC(values_A, values_B))


        



        
        
