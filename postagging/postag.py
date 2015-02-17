__author__ = 'raj'
import json
import sys

def posTagging(modelFile):
    modelFile=open(modelFile,"r")

    dict_classifier=json.loads(modelFile.readline())
    labels=[]
    for item in dict_classifier:
        labels.append(item)
    modelFile.close()
    tieBreaker=labels[0]

    for line in sys.stdin:
        words=line.split()
        wordOfSentenceCounter=0
        words_length=len(words)
        formattedList=[]
        outputTags=[]
        for word in words:
            currentword=word
            if wordOfSentenceCounter==0:
                prevWord="BOS"
                if wordOfSentenceCounter+1< words_length:
                    nextWord=words[wordOfSentenceCounter+1]
                else:
                    nextWord="EOS"
            else:
                prevWord=words[wordOfSentenceCounter-1]

                if wordOfSentenceCounter+1 < words_length:

                    nextWord=words[wordOfSentenceCounter+1]
                else:
                    nextWord="EOS"
            newTestExample="wcurr:"+currentword+" "+"wprev:"+prevWord+" "+"wnext:"+nextWord
            formattedList.append(newTestExample)
            wordOfSentenceCounter+=1


        for sentence in formattedList:

            max=0
            determined_class=""
            sentWords=sentence.split()
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
            outputTags.append(determined_class)

        str=""
        for i in range(0,len(words)):
            str+=words[i]+"/"+outputTags[i]+" "
        print(str)
        sys.stdout.flush()

if __name__=='__main__':
    modelFile=sys.argv[1]
    posTagging(modelFile)