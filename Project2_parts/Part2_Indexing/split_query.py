from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray

#Returns the Keywords, word by word, in a list


#removes special char, a, i etc..
#Returns text words in same order
#returns them at each position of list

def split_query(text):
    
    #filter Fulltext values from stop words : i, a, special char, \n...
    Text_asDoc = [text]
    Text_asKeys =countsArray(Text_asDoc)[0]
    myWords=[]

    #get the filtered full text as list
    for key in Text_asKeys:
        myWords.append(key)

    return myWords