import nltk# Downloads popular datasets/corpora
from nltk.corpus import genesis
from nltk.tokenize import word_tokenize

str1="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Deserunt alias numquam aliquam. Libero, expedita! Sint molestias, officia optio deserunt velit laboriosam veniam provident iure illo. Qui harum voluptates quasi illum ducimus alias pariatur velit tenetur repudiandae assumenda animi, iusto magnam beatae. Saepe corporis velit voluptates veritatis nisi consectetur ullam cumque. Itaque obcaecati placeat at sapiente unde assumenda, molestiae aspernatur nesciunt! Dolorem facere voluptatibus harum inventore voluptatem voluptates dolore molestias? Ipsam quasi at eius nihil tenetur exercitationem quisquam, alias blanditiis aliquam voluptates, obcaecati, nemo voluptas neque omnis saepe soluta dicta officia "

# hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
# for i in hamlet[:40]:
    # print(i,sep=" ",end=" ")
str1tokens=word_tokenize(str1)
# print(str1tokens)

from nltk.probability import FreqDist 
fd=FreqDist()
for word in str1tokens:
    fd[word.lower()]+=1
print(fd.items())
print()
print(fd['lorem'])
print(fd.most_common(10))

print()
from nltk.util import ngrams
str2="like hello there what could you do cuh!"
print(list(nltk.ngrams(nltk.word_tokenize(str2),3)))
