
from nltk.tokenize import sent_tokenize
from textblob import TextBlob

f = open('my.txt','r')
text = f.read().replace('\n', '')
string = str(text)
a = TextBlob(string)

print(a.sentiment_assessments)
print(a.sentiment)

a1 = """Shawn is a very smart human. You should be like shawn. Shawn is the best"""
b1 = """Shawn is a very bad boy. Shawn is evil. Shawn does not belong in this world"""

a2 = TextBlob(a1)
b2 = TextBlob(b1)

print(a2.sentiment)
print(b2.sentiment)
print(b2.sentiment_assessments)
print(b2)