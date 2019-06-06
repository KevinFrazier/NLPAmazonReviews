import pandas as pd
import os
import re
from nltk.stem.porter import *

def writeToFile(data, fileName):

    f = open(fileName,"a+")

    for eachIndex in data:
        f.write(str(eachIndex) + "," + str(data[eachIndex]) + "\n")


    f.close()

def getNgrams(text, n):
    if n == 1:
        return text
    
    ngramList = []
    for i in range(len(text) - (n-1)):
        ngram = text[i:i+n]
        ngramList.append(ngram)
    
    return ngramList
    
def main():
    
    stemmer = PorterStemmer()
    data_directory = "./Reviews.csv"


    data = pd.read_csv(data_directory)

    print("starting")
    unigramDict = {}
    bigramDict = {}
    for index, row in data.iterrows():
        if(index % 10000 == 0):
            print(index)

        text = row["Text"]
        parsedText = re.findall("(\w+)", text)

        #calculate unigram
        for eachWord in parsedText:
            eachWord = stemmer.stem(eachWord)
            eachWord = eachWord.lower()
            if eachWord in unigramDict:
                unigramDict[eachWord] +=1
            else:
                unigramDict[eachWord] =1
        
        parsedText.append("<end>")

        #calculate bigram

        for index in range(len(parsedText)-1):
            bigram = parsedText[index] + "," + parsedText[index+1]
            if bigram in bigramDict:
                bigramDict[bigram] +=1
            else:
                bigramDict[bigram] =1

    writeToFile(unigramDict, "unigramProbabilities.txt")
    writeToFile(bigramDict, "bigramProbabilities.txt")
    

if __name__ == "__main__":
    main()