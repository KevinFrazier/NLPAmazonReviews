import pandas as pd
import os
import re
from nltk.stem.porter import *

def writeToFile(data, fileName):

    print("data")
    print(data)
   

    f = open(fileName,"a+")

    for eachIndex in data:
        print(eachIndex)
        f.write(str(eachIndex) + "\t,\t" + str(data[eachIndex]) + "\n")


    f.close()

def main():
    
    stemmer = PorterStemmer()
    data_directory = "./amazon-fine-food-reviews/Reviews.csv"


    data = pd.read_csv(data_directory)

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
            if eachWord in unigramDict:
                unigramDict[eachWord] +=1
            else:
                unigramDict[eachWord] =1
        
        parsedText.append("<end>")

        #calculate bigram

        for index in range(len(parsedText)-1):
            bigram = (parsedText[index],parsedText[index+1])
            if bigram in bigramDict:
                bigramDict[bigram] +=1
            else:
                bigramDict[bigram] =1

    writeToFile(unigramDict, "unigramProbabilities.txt")
    writeToFile(bigramDict, "bigramProbabilities.txt")
    

if __name__ == "__main__":
    main()