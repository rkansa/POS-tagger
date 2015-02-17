1.Accuracy Of POS tagger on DEV set is **93.0868%**

2.Precision,Recall and F-Score of each entity of NER are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
O      | 0.9511	   | 0.9941 | 0.9721
B-ORG  | 0.7807	   | 0.6252	| 0.6943
B-LOC  | 0.6942	   | 0.6900 | 0.6921
B-PER  | 0.9045    | 0.4729 | 0.6211
I-PER  | 0.8772    | 0.6321 | 0.7347
B-MISC | 0.7011    | 0.3955 | 0.5057
I-ORG  | 0.6817    | 0.4860 | 0.5675
I-LOC  | 0.6611    | 0.5905 | 0.6238
I-MISC | 0.5435    | 0.3409 | 0.4187

#Overall Fscore:0.9298

3.When Naive Bayes classifier is used for NER tagging,the performance decreases significantly for all entities except "O".The results are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
O      | 0.9343	   | 0.9846 | 0.9588
B-ORG  | 0.5540	   | 0.6134	| 0.5822
B-LOC  | 0.5809	   | 0.4776 | 0.5242
B-PER  | 0.8198    | 0.4320 | 0.5659
I-PER  | 0.7    | 0.6845 | 0.6921
B-MISC | 0.7837    | 0.0651 | 0.1203
I-ORG  | 0.6151    | 0.3382 | 0.4364
I-LOC  | 0.8450    | 0.1780 | 0.29411
I-MISC | 0.4396    | 0.0779 | 0.1324

#Overall FScore=0.9046

Naive bayes assumes that each feature occurs independently of the other features,while NER tagging takes into context the previous and the later words(Sliding window) to determine the entity of the current tag, which gives it a better Fscore in comparison.Thus for each word we have 3 relevant features at our disposal,which provides better supervised learning as against the conditional independent assumption of Naive Bayes.The Fscore for "O" entity does not reduce as drastically as other tags when Naive Bayes classifier is used,because "O" has a large prior probability compared to others and as most of the data has entity "O",a large chunk of the data is correctly classified as "O".