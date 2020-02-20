import collections
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults
#%matplotlib inline

file = open('newFile.csv')
a = file.read()
stopwords = set(line.strip() for line in open ('stopwords.txt'))
stopwords = stopwords.union(set(['change', 'at', 'actions','and','with','of','mm', 'by', 'no']))

wordcount = {}

ignore = {'change','Diabetes'}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words
# Draw a bar chart
'''lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')


file = open("countries.csv","r+")
a = file.read()
stopwords = set(line.strip() for line in open ('stopwords.txt'))
stopwords = stopwords.union(set(['change', 'at', 'actions','and','with','of', 'by', '&', 'no', 'business', 'area', 'region', 'as','international','operations','novo', 'nordisk','a/s']))

wordcount = {}

ignore = {'change','the','a','if','in','it','of','or', 'A/S', 'Novo', 'Nordisk', 'Regulatory', 'local', 'Quality', 'Dept.','FLIT', 'Dept.', 'Operations', 'Diabetes', 'novo', 'nordisk', 'operations', 'a/s'}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("/", "")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')




file = open("STAFF.CSV","r+")
a = file.read()
stopwords = set(line.strip() for line in open ('stopwords.txt'))
stopwords = stopwords.union(set(['change', 'at', 'actions','and','with','of','mm', 'you', 'is', 'this', 'group', 'by', '&', 'no', 'business', 'area', 'region', 'as','international','operations','novo', 'nordisk','a/s','that','subject','sent']))

wordcount = {}

ignore = {'change','the','a','if','in','it','of','or', 'A/S', 'Novo', 'Nordisk', 'Regulatory', 'Dept.', 'FLIT', 'Dept.', 'Operations', 'Diabetes', 'novo', 'nordisk', 'operations', 'a/s'}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("/", "")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')
'''