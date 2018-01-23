import nltk
from nltk.stem.snowball import *

input = open('input.txt','r+') #open a .txt file
sentence = input.read() #read a sentence from the file
print('Input             : ' + sentence)

output = open('output.txt','a+') #create or modify existing .txt
output.write('\n')

tokens = nltk.word_tokenize(sentence)
wcount = len(tokens) #number of word in sentence
print('Tokenized Sentence: ' + str(tokens))
print('Word Count        : ' + str(len(tokens)))

stemmer = SnowballStemmer("english") #initializing the stemmer using Snowball Stemmer
stemmed = [stemmer.stem(word) for word in tokens]   #Stemming every words in tokenized sentence
print('Stemmed Sentence  : ' + ' '.join(stemmed))

#writing output.txt
output.write('Tokenized Sentence: ' + str(tokens) + '\n')
output.write('Word Count        : ' + str(len(tokens)) + '\n')
output.write('Stemmed Sentence  : ' + ' '.join(stemmed) + '\n')