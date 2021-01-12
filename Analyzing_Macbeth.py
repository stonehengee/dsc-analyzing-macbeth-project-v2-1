import requests
macbeth = requests.get('http://www.gutenberg.org/cache/epub/2264/pg2264.txt').text

#cuts off the text before the beginning of the play
macbeth = macbeth[macbeth.index("David Reed")+len("David Reed"):]

print(type(macbeth))
print(len(macbeth))
print(macbeth[:50])

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# Your code here


# Pseudo-code outline
'''

'''

# Split the transcript into words
macbeth = macbeth.split()

# Create a dictionary

m_word_dictionary = {}

# Iterate through the text of Macbeth

for word in macbeth:
    word = word.title()
    if m_word_dictionary.get(word):

# Update word counts

        m_word_dictionary[word] += 1
    else:
        m_word_dictionary[word] = 1

# Sort words by counts in descending order

# print(dict(sorted(m_word_dictionary.items(), key=lambda item: item[1])))
most_common_words = {}
for words in sorted(m_word_dictionary, key=m_word_dictionary.get, reverse=True)[:25]:
    most_common_words[words] = m_word_dictionary[words]

print(len(most_common_words))
# Create Bar Graph

x=[]
y=[]
for words in most_common_words.keys():
    x.append(words)
    y.append(most_common_words[words])
    
plt.figure(figsize=(15, 6))

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("The Frequency of the 25 Most Commonly Used Words in Macbeth")
plt.bar(x, y, label="Frequency of Words in Macbeth")
plt.legend()
plt.show()
# Include descriptive titles and labels