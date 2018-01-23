import nltk

sentence = 'I am going to take NLP class next semester'
tokens = nltk.word_tokenize(sentence)

for word in tokens: #print length of words in tokens
    print(str(len(word)) + ' ')