#returns docID where the word is contained

def docID(docs,word):
    
    inverted_index = {}

    for i, doc in enumerate(docs):
        for term in doc.split():
            if term in inverted_index:
                inverted_index[term].add(i)
            else: inverted_index[term] = {i}
    
    if word in inverted_index.keys():
        posting_list = inverted_index[word]
        return posting_list
    
    #print(posting_list)
    return {}