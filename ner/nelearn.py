
import sys
__author__ = 'raj'

sys.path.insert(0,'../')
from perceplearn import percepLearn

training=sys.argv[1]
modelFile=sys.argv[2]


formattedtr="formattedNERtraining.txt"
trainingFile=open(training,"r+",errors='ignore')
formattedTrainingfile=open(formattedtr,"w+")

for line in trainingFile.readlines():
    words=line.split()
    wordOfSentenceCounter=0
    words_length=len(words)
    for word in words:
        currentWord=word.split("/")[0]
        if currentWord.islower():
            wordShape="a"
        elif currentWord.isupper():
            wordShape="A"
        else:
            wordShape="Aa"
        currentTag=word.split("/")[1]
        index=word.rfind("/",0,len(word))
        currentNER=word[index+1:]
        if wordOfSentenceCounter==0:
            prevWordMinusTags="BOS"
            prevTag="BOS"
            prevNER="BOS"
            if wordOfSentenceCounter+1< words_length:
                nextWord=words[wordOfSentenceCounter+1]
                nextWordminusTags=nextWord.split("/")[0]
                nextTag=nextWord.split("/")[1]
            else:
                nextWordminusTags="EOS"
                nextTag="EOS"
        else:
            prevWord=words[wordOfSentenceCounter-1]
            prevWordMinusTags=prevWord.split("/")[0]
            prevTag=prevWord.split("/")[1]
            index1=prevWord.rfind("/",0,len(prevWord))
            prevNER=prevWord[index1+1:]
            if wordOfSentenceCounter+1< words_length:
                nextWord=words[wordOfSentenceCounter+1]
                nextWordminusTags=nextWord.split("/")[0]
                nextTag=nextWord.split("/")[1]
            else:
                nextWordminusTags="EOS"
                nextTag="EOS"
        wordOfSentenceCounter+=1

        formattedTrainingfile.write(currentNER+" ")
        formattedTrainingfile.write("wcurr:"+currentWord+" ")
        formattedTrainingfile.write("wcurrTag:"+currentTag+" ")
        formattedTrainingfile.write("wprevTag:"+prevTag+" ")
        formattedTrainingfile.write("wprev:"+prevWordMinusTags+" ")
        formattedTrainingfile.write("wnextTag:"+nextTag+" ")
        formattedTrainingfile.write("wnext:"+nextWordminusTags+" ")
        formattedTrainingfile.write("wordShape:"+wordShape+" ")
        formattedTrainingfile.write("wprevNER:"+prevNER+" ")
        formattedTrainingfile.write("\n")

formattedTrainingfile.close()
percepLearn(formattedtr,modelFile)






