1.Accuracy Of POS tagger on DEV set is **94.8799%**

2.Precision,Recall and F-Score of each entity of NER are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
ORG  | 0.7784	   | 0.7857	| 0.7820
LOC  | 0.7827	   | 0.6626 | 0.7176
PER  | 0.900    | 0.7962 | 0.8449
MISC | 0.6948    | 0.4808 | 0.5683

#Overall Fscore:0.7660

3.When Naive Bayes classifier is used for NER tagging,the performance decreases significantly.The results are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
ORG  | 0.6136	| 0.4840	| 0.5411
LOC  | 0.7065| 0.4380 | 0.54075
PER  | 0.7880    | 0.3690 | 0.5026
MISC | 0.4333    | 0.029 | 0.054


Naive bayes assumes that each feature occurs independently of the other features,while NER tagging takes into context the previous and the later words(Sliding window) to determine the entity of the current tag, which gives it a better Fscore in comparison.
Thus for each word we have 3 relevant features at our disposal,which provides better supervised learning as against the conditional independent assumption of Naive Bayes.In part of Speech and NER tagging a word has some sort of dependency on it's successor and 
predecessor,as a result of which the perceptron classifies more accurately,also features such as case sensitivity which helps to identify entities such as ORG (organization) and PER(Person),suffixes of word plays a good role in classifying the word correctly.This features
can be easily provided in the perceptron.Apart from this perceptron improves it's learning with each iteration while Naive Bayes makes only one pass through the data.All these reasons combined makes Averaged 
Perceptron a better classifier for NER and POS tagging