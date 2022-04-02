# lowercases your text (set lowercase=false if you don’t want lowercasing)
# uses utf-8 encoding
# performs tokenization (converts raw text to smaller units of text)
# uses word level tokenization (meaning each word is treated as a separate token)
# ignores single characters during tokenization (say goodbye to words like ‘a’ and ‘I’)

from sklearn.feature_extraction.text import CountVectorizer

# overwrite my tokenizer to eliminate special characters
import re
def my_tokenizer(text):
    # create a space between special characters 
    text=re.sub("(\\W)"," \\1 ",text)
    # split based on whitespace
    return re.split("\\s+",text)






#takes words of each document at evey position  seperately : at pos 0 : text of doc1    at pos 1 : text of doc2     at pos 2 : doc3
documents=["My Name Is Charbel? Yes it is Charbel", "Is my name Charbel?", "No I dont think so"]

# ngram_range = (1, 3) means we are using 
# unigram : 1 word: "my", 
# bi-gram: 2 word : "my name" 
# trigram: 3-words groups. Basically, we are using ith gram in the given range.
count_vect = CountVectorizer(ngram_range=(1,1) ) 

final_counts = count_vect.fit_transform(documents)

# returns : {'my': 2, 'name': 3, 'is': 1, 'charbel': 0}
print(count_vect.vocabulary_)



#print(final_counts.shape)

#array to be used to compute IR/IDF weights
print(final_counts.toarray())

# the type of count vectorizer <class 'scipy.sparse._csr.csr_matrix'>
#print("the type of count vectorizer",type(final_counts))


#print(final_counts)


# Resume 
#So now we can get the 
# number of times a word is in a same document
# number of times a word is in all documents
