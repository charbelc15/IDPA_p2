from Project2_parts.Part2_Indexing.docID import docID


def index_Query_TF(keywords_list, documents,AllAugmentedvectorsTF):
    
    #dictionary of 
    # keys: (String) keyword 
    # values : (dictionary) docIDs where keyword is , weight of the word at that doc
    Keywords_docIDs={}
    
    
    for keyword in keywords_list:
        docIDs = docID(documents,keyword)
        keywordlist=[] #first val: docID, second val: weight at doc
        for ID in docIDs:
            list=[]
            #print(ID)
            for element in AllAugmentedvectorsTF[ID]:
                if(element[0]==keyword):
                    list.append(ID)
                    list.append(element[1])
                    keywordlist.append(list)
                    Keywords_docIDs[keyword] = keywordlist

            
    
    return Keywords_docIDs
        

