import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import wordpunct_tokenize


corpus="My dog \"sarma's\" diagphram and liver comes out often! he loovvez it. And his cat gf too"
documents=sent_tokenize(corpus)
# print(documents)
for document in documents:
    # print(word_tokenize(document))
    # print(wordpunct_tokenize(document)) #punctuations get tokenized too
    pass
#:only last fullstop gets tokenized

from nltk.tokenize import TreebankWordTokenizer
print(TreebankWordTokenizer().tokenize(corpus))

