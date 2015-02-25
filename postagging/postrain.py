__author__ = 'raj'
import sys

sys.path.insert(0,'../')
from perceplearn import percepLearn


training=sys.argv[1]
modelFile=sys.argv[2]

formattedtr="formattedPOStraining.txt"
trainingFile=open(training,"r+")
formattedTrainingfile=open(formattedtr,"w+")


for line in trainingFile.readlines():
    words=line.split()

    wordOfSentenceCounter=0
    words_length=len(words)
    for word in words:
        currentword=word.split("/")[0]
        index=word.rfind("/",0,len(word))
        tag=word[index+1:]
        suffix3=currentword[-3:]
        suffix2=currentword[-2:]

        if wordOfSentenceCounter==0:
            prevWord="BOS"
            prevwordminusTag=prevWord
            if wordOfSentenceCounter+1< words_length:
                nextWord=words[wordOfSentenceCounter+1]
                nextWordminusTag=nextWord.split("/")[0]
                nextWordTag=nextWord.split("/")[1]
            else:
                nextWordminusTag="EOS"

        elif wordOfSentenceCounter==1:
            prevWord=words[wordOfSentenceCounter-1]
            prevwordminusTag=prevWord.split("/")[0]
            prevTag=prevWord.split("/")[1]
            if wordOfSentenceCounter+1 < words_length:
                nextWord=words[wordOfSentenceCounter+1]
                nextWordminusTag=nextWord.split("/")[0]
            else:
                nextWordminusTag="EOS"
            nextWordTag=nextWord.split("/")[1]
        else:
            prevWord=words[wordOfSentenceCounter-1]
            prevwordminusTag=prevWord.split("/")[0]
            prevTag=prevWord.split("/")[1]
            if wordOfSentenceCounter+1 < words_length:

                nextWord=words[wordOfSentenceCounter+1]
                nextWordminusTag=nextWord.split("/")[0]
                nextWordTag=nextWord.split("/")[1]
            else:
                nextWordminusTag="EOS"

        wordOfSentenceCounter+=1

        formattedTrainingfile.write(tag+" ")
        formattedTrainingfile.write("wcurr:"+currentword+" ")
        formattedTrainingfile.write("wprev:"+prevwordminusTag+" ")
        formattedTrainingfile.write("wnext:"+nextWordminusTag+" ")
        formattedTrainingfile.write("suffix3:"+suffix3+" ")
        formattedTrainingfile.write("suffix2:"+suffix2+" ")
        formattedTrainingfile.write("\n")
formattedTrainingfile.close()
percepLearn(formattedtr,modelFile)


