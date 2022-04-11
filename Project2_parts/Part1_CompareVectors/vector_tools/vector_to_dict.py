
# Transform 2D vector (augmented vector) to dictionnary 
# each inner vector
#       1st val : key
#       2nd val : value 

# 2 elements with the same key --> add their values

def vector_to_dict(vector):
    dict={}
    for element in vector:
        key=element[0]
        val=element[1]
        if key in dict.keys(): # 2 elements with the same key --> add their values
            dict[key] +=val
        else:    
            dict[key]=val

    return sorted(dict.items())

