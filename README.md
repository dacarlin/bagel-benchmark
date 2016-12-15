# Predicting effects of mutations on enzyme function, stability, and structure using a combination of molecular modeling and machine learning 

## Molecular modeling protocols

Each molecular modeling protocol is a self-contained directory containing all the required scripts to run the protocol. Currently, most protocols have

1. a `make_list.py` preprocessing script that creates the input files for parallelization 
1. a submit script `sub.sh` to submit the parallel runs to SLURM
3. two directories, `logs` and `out`, where the output goes 
4. a `data_processing.py` script to transform the output of the protocol into a feature set

Each protocol has its own specialized version of each of these scripts, to account for all the different kinds of output the protocol produces. Details of each protocol are below. 

### Rosetta protocols 

#### Benchmark modeling set 

+ Files: `rosetta_runs/benchmark`

+ This feature set contains 45 features from Rosetta's enzyme design protocols, using scorefunction Talaris 2014. One hundred structures for each single point mutant are created using the `MutateResidue` mover, repacked and minimized by `EnzRepackMinimize` mover (10 Monte Carlo trials to minimize total system energy), scored using `-jd2:enzdes_out`. Features from the lowest 10 structures for each mutant are averaged. 

+ Run time on Cabernet: about 6 days for all 9000 possible point mutants 

#### Shells (`shells`) 

+ Files: `rosetta_runs/benchmark`

+ Same as benchmark protocol, except that here constraint energy is optimized by Monte Carlo and also there is a constraint optimization step where the protein is mutated to all alanine and constraint energy is minimized. 

+ Run time on Cabernet: about 6 days for all 9000 possible point mutants 

#### Reduced sampling protocol (`new_protocol`) 

+ Files: `rosetta_runs/new_protocol`

+ This feature set contains 45 features from Rosetta's enzyme design protocols. Ten structures for each single point mutant are created using the `MutateResidue` mover, repacked and minimized by `EnzRepackMinimize` mover (10 Monte Carlo trials to minimize total system energy), scored using `-jd2:enzdes_out`.

+ Run time on Cabernet: about 8 hours for all 9000 possible point mutants 

### FoldX protocols 

### Position-specific scoring matrix (PSSM) feature set  

+ Files: `foldx_runs/pssm`

+ This feature set contains 13 features output by the position-specific scoring matrix (PSSM) function of FoldX

+ Run time on Cabernet: about 24 hours for all possible point mutants 

## Machine learning 

### Prediction of kinetic constants and thermal stability (regression) 

+ Original implementation of algorithms used in [our paper describing the combination of molecular modeling and machine learning to predict enzyme kinetic constants](http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0147596) by Xiaokang Wang (Ilias Tagkopoulos, UC Davis)

+ Implementation in Python (using `scikit-learn`) of the elastic net algorithm used in the PLOS paper (elastic net with bagging) allows comparison of the various feature sets for prediction of enzyme properties (see `machine_learning/elastic_net_with_bagging`) 

### Prediction of protein expression in *Escherichia coli* (classification) 

+ SVM classifiers for prediction of protein expression from above feature sets (see `machine_learning/protein_expression`) 
