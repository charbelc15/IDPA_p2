from Project2_parts.Part2_Indexing.docID import docID
import operator


def order_docs(Keywords_docIDs):

    ordered_docs={}

    for key in Keywords_docIDs:
        value = Keywords_docIDs[key]

        for val in value:
            docID=val[0]
            word_weight=val[1]
        
            #if word_weight bigger than one before --> doc's word weight updated
            if(docID in ordered_docs.keys()):
                if(word_weight>ordered_docs[docID]):
                     ordered_docs[docID]=word_weight
            
            #if docID's word_weight hasnt been inserted it 
            else:
                ordered_docs[docID]=word_weight
        
    #order dict. by descending order of values
    ordered_docs = dict( sorted(ordered_docs.items(), key=operator.itemgetter(1),reverse=True))

    return ordered_docs
            
        


