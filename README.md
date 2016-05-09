# Predicting effects of mutations on enzyme function, stability, and structure using a combination of molecular modeling and machine learning 

## Contents 

### Prediction of kinetic constants from `enzyme_design` feature set

+ Original benchmark: implementation of algorithms used in [our PLOS paper](http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0147596) in Python using scikit-learn (originally implemented by Xiaokang Wang in R)

+ Multi-classifier feature sorting pipeline: systematically sorts Rosetta feature metrics by feature, picks lowest 10% of that feature, and trains multiple classifiers, reports which is best. Currently for kinetic constants only. Currently implemented elastic net with coordinate descent, elastic net with stochastic gradient descent, and elastic net with bagging. 

### Prediction of protein thermal stability and expression 

+ Elastic nets for prediction of protein melting temperature from `ddg_monomer` and `enzyme_design` feature sets 

+ SVM classifiers for prediction of protein expression from `ddg_monomer` and `enzyme_design` feature sets 
