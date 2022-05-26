# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

#use regex to remove punctuations
import re

#read contents of file in directory inputed
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename) as f:
        contents = f.read()
    
    return (str(contents))

#gets the output from read file function then counts the occurence of each word
def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    texts=text.strip()
    texts= texts.lower()
    texts= re.findall(r'\w+',texts)
    counts = dict()
    for word in texts:
      if word in counts:
        counts[word]+=1
      else:
        counts[word]=1
    return (dict(counts))


#echo count_words return value 
print (count_words())