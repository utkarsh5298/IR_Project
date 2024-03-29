from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
file = [None]*2572

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed
stop_words = set(stopwords.words('english'))
for i in range(2572): #2572
    try:
        file[i] = open("A:/IR1/F5000/New Folder/file"+str(i+1)+".txt",encoding="ISO-8859-1")
        line = file[i].read()
        text = "".join([ch for ch in line if ch not in [",",".","(",")","-",":","?","#","[","]","*",";","§","\"","`","/","_","'",
                                                    "1","2","3","4","5","6","7","8","9","0","!","{","}"]])
        tokens = word_tokenize(text)
        stems = stem_tokens(tokens, stemmer)
        for r in stems:
            if not r in stop_words:
                appendFile = open('A:/IR1/F5000/New Folder/f-t'+str(i+1)+'.txt', 'a')
                appendFile.write(" "+r)
                appendFile.close()
    except Exception: pass

    def freq(str1):
        str_list = str1.split()
        unique_words = set(str_list)
        for words in unique_words:
            appendFile = open('A:/IR1/F5000/New Folder/freq-t'+str(i+1)+'.txt', 'a')   
            words = words.lower()
            appendFile.write( words + ':'+str(str_list.count(words)+1)+"\n" )
            appendFile.close()
for i in range(2572): #2572
    try:
        file[i] = open("A:/IR1/F5000/New Folder/f-t"+str(i+1)+".txt",encoding="ISO-8859-1")
        line = file[i].read()
        words = word_tokenize(line)
        freq(line)
    except Exception: pass