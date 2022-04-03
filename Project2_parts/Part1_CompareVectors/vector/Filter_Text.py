from Project2_parts.Part1_CompareVectors.term_weighting.countsArray import countsArray


#removes special char, a, i etc..
#Returns text words in same order

def Filter_Text(text):
    
    #filter Fulltext values from stop words : i, a, special char, \n...
    Text_asDoc = [text]
    Text_asKeys =countsArray(Text_asDoc)[0]
    Text_Filtered=""

    #get the filtered full text as STRING from KEYS of countsArray's wordpositions result
    for key in Text_asKeys:
        Text_Filtered+= key + " "

    return Text_Filtered