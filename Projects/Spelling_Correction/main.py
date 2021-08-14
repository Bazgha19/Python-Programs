#Spelling Correction

from textblob import TextBlob

word=input("Enter Your word: ")

c=TextBlob(word)
print(c.correct())
