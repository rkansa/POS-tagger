1.Accuracy Of POS tagger on DEV set is **94.8799%**

2.Precision,Recall and F-Score of each entity of NER are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
ORG  | 0.6980	   | 0.6586	| 0.
LOC  | 0.7578	   | 0.6646 | 0.
PER  | 0.8223    | 0.7348 | 0.
MISC | 0.592    | 0.3325 | 0.

#Overall Fscore:0.6910

3.When Naive Bayes classifier is used for NER tagging,the performance decreases significantly for all entities except "O".The results are as follows:

Entity | Precision | Recall | F-Score
-------|-----------|--------|------------------
ORG  | 0.5540	   | 0.6134	| 0.5822
LOC  | 0.5809	   | 0.4776 | 0.5242
PER  | 0.8198    | 0.4320 | 0.5659
MISC | 0.7837    | 0.0651 | 0.1203


Naive bayes assumes that each feature occurs independently of the other features,while NER tagging takes into context the previous and the later words(Sliding window) to determine the entity of the current tag, which gives it a better Fscore in comparison.
Thus for each word we have 3 relevant features at our disposal,which provides better supervised learning as against the conditional independent assumption of Naive Bayes.
.