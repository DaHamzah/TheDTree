import nltk
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords


response = urllib.request.urlopen('https://www.bt.dk/udland/angreb-i-tyskland-efterforskes-som-terror-gerningsmands-mor-fundet-doed')
html = response.read()
soup = BeautifulSoup(html,'html.parser')

#kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text(strip = True)
#print(text)
tokens = [t for t in text.split()]
#print(tokens)

sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)

#But how will you cover for the Twitter Scrapping part

#NB. If you publish work that uses NLTK, please cite the NLTK book as follows:, Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.