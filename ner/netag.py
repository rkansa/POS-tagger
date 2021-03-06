__author__ = 'raj'

import json
import sys
import codecs

def netag(modelFile):
    modelFile=open(modelFile,"r",errors='ignore')

    dict_classifier=json.loads(modelFile.readline())
    labels=[]
    for item in dict_classifier:
        labels.append(item)
    modelFile.close()
    tieBreaker=labels[0]
    sys.stdin=codecs.getreader('utf-8')(sys.stdin.detach(),errors='ignore')
    for line in sys.stdin:
        prevNer="BOS"
        words=line.split()
        wordOfSentenceCounter=0
        words_length=len(words)
        formattedList=[]
        outputTags=[]
        for word in words:
            currentWord=word.split("/")[0]
            currentTag=word.split("/")[1]
            if currentWord.islower():
                wordShape="a"
            elif currentWord.isupper():
                wordShape="A"
            else:
                wordShape="Aa"
            if wordOfSentenceCounter==0:
                prevWordMinusTags="BOS"
                prevTag="BOS"
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
                if wordOfSentenceCounter+1< words_length:
                    nextWord=words[wordOfSentenceCounter+1]
                    nextWordminusTags=nextWord.split("/")[0]
                    nextTag=nextWord.split("/")[1]
                else:
                    nextWordminusTags="EOS"
                    nextTag="EOS"
            newTestExample="wcurr:"+currentWord+" "+"wcurrTag:"+currentTag+" "+"wprevTag:"+prevTag+" "+"wprev:"+prevWordMinusTags+" "+"wnextTag:"+nextTag+" "+"wnext:"+nextWordminusTags+" "+"wordShape:"+wordShape
            formattedList.append(newTestExample)
            wordOfSentenceCounter+=1

        for sentence in formattedList:

            max=0
            determined_class=""
            sentWords=sentence.split()
            sentWords.append("wprevNER:"+prevNer)
            predictor={}
            for c in labels:
                predictor.setdefault(c,0)
            for each_class in labels:
                for word in sentWords:
                    if word not in dict_classifier[each_class]:
                        dict_classifier[each_class][word]=0
                    predictor[each_class]+=int(dict_classifier[each_class][word])

            for key in predictor.keys():
                if predictor[key]>max:
                    max=predictor[key]
                    determined_class=key
            if determined_class=="":
                determined_class=tieBreaker
            prevNer=determined_class
            outputTags.append(determined_class)

        str=""
        for i in range(0,len(words)):
            str+=words[i]+"/"+outputTags[i]+" "
        print(str)
        sys.stdout.flush()


if __name__=='__main__':
    modelFile=sys.argv[1]
    netag(modelFile)