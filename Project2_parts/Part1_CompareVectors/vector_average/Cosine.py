import numpy as np
import math 
from numpy import linalg as LA
from scipy.linalg import sqrtm

def Cosine(dictA,dictB):

    values_A=[]
    values_B=[]

    for element in dictA:
        valueA = element[1]
        values_A.append(valueA)
    
    for element in dictB:
        valueB = element[1]
        values_B.append(valueB)

    # Get numerator
    numerator=0
    
    for i in range(0,len(values_A)):
        product = values_A[i]*values_B[i]
        numerator += product

    # Get denomenator
    

    sum1=0
    for i in range(0,len(values_A)):
        sum1 += np.power( values_A[i] ,2)
    sum2=0
    for i in range(0,len(values_B)):
        sum2 += np.power( values_B[i] ,2)

    product_denom=sum1*sum2
    denomenator = np.power( product_denom , 0.5 )

     #!! if all terms are of 0 factor --> denominator will be 0 --> return a 0 similarity value
    if denomenator==0:
        return 0
    Sim = np.divide(numerator,denomenator)

    return Sim

