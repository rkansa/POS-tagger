__author__ = 'raj'

import json
import sys
trainingFile=sys.argv[1]
modelFile=sys.argv[2]


def percepLearn(trainingFile,modelFIle):
    super_dict={}
    super_dict_avg={}

    classes=[]
    classes_Avg=[]
    inputfile=open(trainingFile,"r")
    initialError=0
    finalError=0
    deltaError=1
    #Initialize the weight vector
    for line in inputfile.readlines():
        words=line.split()

        otherwords=words[1:]
        if words[0] not in classes:
            classes.append(words[0])
            classes_Avg.append(words[0])

    inputfile.close()
    inputfile=open(trainingFile,"r")
    for line in inputfile.readlines():
        words=line.split()
        otherwords=words[1:]
        for c in classes:
            if c not in super_dict:
                temp_dict={}
                temp_dict_avg={}
                super_dict[c]=temp_dict
                super_dict_avg[c]=temp_dict_avg
            for word in otherwords:
                if word not in super_dict[c]:
                    super_dict[c][word]=0
                    super_dict_avg[c][word]=0

    deterministic_predictor=classes[0]
    inputfile.close()
    counter=0
    iteration=0
    MAX_ITERATIONS=20
    #Learn through Iterations
    while deltaError>0.0001 and iteration<MAX_ITERATIONS:
        iteration+=1
        print(iteration)
        lineCount=0
        errorCount=0
        inputfile=open(trainingFile,"r")
        for line in inputfile.readlines():
            max=0
            lineCount+=1
            determined_class=""
            words=line.split()
            correct_class=words[0]
            predictor={}
            for c in classes:
                predictor.setdefault(c,0)
            otherwords=words[1:]
            for each_class in classes:
                for word in otherwords:
                    predictor[each_class]+=int(super_dict[each_class][word])
            for key in predictor.keys():
                if predictor[key]>max:
                    determined_class=key
            if determined_class=="":
                determined_class=deterministic_predictor


            if determined_class!=correct_class:
                errorCount+=1
                for word in otherwords:
                    super_dict[correct_class][word]+=1
                    super_dict[determined_class][word]-=1
                    super_dict_avg[correct_class][word]+=counter*1
                    super_dict_avg[determined_class][word]-=counter*1

            counter+=1


        inputfile.close()
        finalError=float(errorCount/lineCount)

        print("Error "+str(finalError))
        deltaError=abs(finalError-initialError)
        initialError=finalError
        print("Delta Error "+str(deltaError))
    for c in classes:
        for word in super_dict_avg[c]:
            super_dict_avg[c][word]=super_dict[c][word]-(1/counter)*super_dict_avg[c][word]

    model=open(modelFile,"w+")

    json.dump(super_dict_avg,model)

if __name__=='__main__':
    percepLearn(trainingFile,modelFile)




