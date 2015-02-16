__author__ = 'raj'
import json
import sys

modelFile=sys.argv[1]



def percepClassify(modelFile):
    modelFile=open(modelFile,"r")

    dict_classifier=json.loads(modelFile.readline())
    labels=[]
    for item in dict_classifier:
        labels.append(item)
    modelFile.close()
    tieBreaker=labels[0]

    for line in sys.stdin:
            max=0
            determined_class=""
            words=line.split()
            predictor={}
            for c in labels:
                predictor.setdefault(c,0)
            otherwords=words[0:]
            for each_class in labels:
                for word in otherwords:
                    if word not in dict_classifier[each_class]:
                        dict_classifier[each_class][word]=0
                    predictor[each_class]+=int(dict_classifier[each_class][word])
            for key in predictor.keys():
                if predictor[key]>max:
                    determined_class=key
            if determined_class=="":
                determined_class=tieBreaker
            print(determined_class)
            sys.stdout.flush()

if __name__=='__main__':
    percepClassify(modelFile)

