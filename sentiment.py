# https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk



import nltk
text ="""Hello Mr. Smith, how are you doing today? no? no didnt? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
print(text)
#nltk.download('punkt')

# Sentence tokenization
from nltk.tokenize import sent_tokenize
tokenized_text= sent_tokenize(text)
print(tokenized_text)

# Word tokenization
from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(text)
print(tokenized_word)

#Frequency distribution
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)
print(fdist.most_common(2))
#Frequency distribution plot
import matplotlib.pyplot as plt
#fdist.plot(30, cumulative = False)
#plt.show()

#stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words("english"))
print(stop_words)

#removing stopwrods
filtered_sent=[]
for w in tokenized_word:
    if w not in stop_words:
        filtered_sent.append(w)
print("tokenized sentence:", tokenized_word)
print("filtered sentence: ", filtered_sent)

# steamming
# Example: Connecting = connect
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
stemmed_words = []
for w in filtered_sent:
    stemmed_words.append(ps.stem(w))

print("filtered sentence:", filtered_sent)
print("stemmed sentence: ", stemmed_words)

# Lemmatization
# Example: Better = good
from nltk.stem.wordnet import WordNetLemmatizer
#nltk.download('wordnet')
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()
word = "flying"
print("Lematized Word:", lem.lemmatize(word, "v"))
print("Stemmed Word:", stem.stem(word))

# POS Tagging
nltk.download('averaged_perceptron_tagger')
sent = "Albert Einstein was born in Ulm, Germany in 1879."
tokens = nltk.word_tokenize(sent)
print(tokens)

print(nltk.pos_tag(tokens))