# Machine learning for prediction of enzyme biophysical parameters from computational models

## Software used

+ scikit-learn for machine learning
+ rosetta for protein models
+ foldx for protein models

## Experimentally-determined parameters

Parameter name | Parameter symbol | Type | Limits of detection | Unit | reported for | |
---|---
soluble expression | | boolean | 0 or 1 | None | all mutants |
melting temperature | T<sub>m</sub> | real | 20-60 |  ˚C | express and kcatkm > LOD |
Turnover rate | <i>k<sub>cat</sub></i> | real | 1-2e6 | min<sup>&minus;1</sup> | express and within LOD |
Michaelis constant | KM | real | 0.05-200 | mM | express and within LOD |  
Efficiency | kcat/KM | real | >10 | M<sup>&minus;1</sup>&nbsp;min<sup>&minus;1</sup> | express and within LOD |

## Experimentally-determined parameters for machine learning 

Parameter name | Parameter symbol | Type | Range | Unit | reported for | Description |
---|---
soluble expression | | boolean | 0 or 1 | None | all mutants |
melting temperature | T<sub>m</sub> | real | [-10,&nbsp;10] | express and kcatkm > LOD | Relative to WT
Turnover rate | <i>k<sub>cat</sub></i> | real | [-5,&nbsp;1] | min<sup>&minus;1</sup> | express and within LOD |
Michaelis constant | KM | real | [-2,2] | mM | express and within LOD |  
Efficiency | kcat/KM | real | [-5,5] | M<sup>&minus;1</sup>&nbsp;min<sup>&minus;1</sup> | express and within LOD |


## Feature sets

Feature name | Feature set | Features (per mutant) | Brief description | Software | Reference
---|---
enzyme_design | | ~50 | Features currently used for enzyme design, including individual terms for ligand and catalytic residues, as well as ligand interface score | Rosetta | [Leaver-Fay PLOS 2013]
ddg_monomer | | 1 | ddG calculation based on Poisson-Boltzman weighted average of 50 simulations | Rosetta | [Kellogg PLOS]
position_scan | | 1 | ddG calculation based on ~20 score terms after energy minimization | FoldX | [FoldX website](http://foldxsuite.crg.eu/command/PositionScan)
reference | | 2 | Evolutionary information | BLOSUM, BioPython |


## Feature set details

### Evolutionary information

Feature name | Feature | Description |
---|---
blosum | Blosum score | Blosum score for the substitution
conservation | Percent conservation | Percent in Pfam alignment

### Structural

Feature name | Feature | Description |
---|---
distance | Distance from active site | CA distance from the ligand centroid of native residue


### Rosetta

Feature name | Feature set | Type | Range | Software | Reference
---|---
fa_rep | enzyme_design | Full-atom repulsion  
hbond_sc | Count of sidechain H-bonds
SR_1_burunsat_pm | Count of buried, unsatisfied polar contacts, E353
SR_1_fa_rep | Full-atom repulsion, nucleophile
SR_1_hbond_pm | Count of H-bonds, nucleophile
SR_1_hbond_sc | Energy of H-bonds, nuleophile
SR_1_nlpstat_pm |
SR_1_pstat_pm |
SR_1_total_score | Energy, nucleophile
SR_2_burunsat_pm | Count of buried, unsatisfied polar contacts, E164
SR_2_fa_rep |
SR_2_hbond_pm |
SR_2_hbond_sc |
SR_2_nlpstat_pm |
SR_2_pstat_pm |
SR_2_total_score |
SR_3_burunsat_pm | Count of buried, unsatisfied polar contacts, E353
SR_3_fa_rep |
SR_3_hbond_pm |
SR_3_hbond_sc |
SR_3_nlpstat_pm |
SR_3_pstat_pm |
SR_3_total_score |
SR_4_burunsat_pm | Count of buried, unsatisfied polar contacts, Y295
SR_4_fa_rep |
SR_4_hbond_pm |
SR_4_hbond_sc |
SR_4_nlpstat_pm |
SR_4_pstat_pm |
SR_4_total_score |
SR_5_burunsat_pm | Count of buried, unsatisfied polar contacts, pNPG
SR_5_dsasa_1_2 | Change in solvent-accessible surface area on binding
SR_5_fa_rep |
SR_5_hbond_pm |
SR_5_hbond_sc |
SR_5_interf_E_1_2 | Interface energy
SR_5_total_score |
tot_burunsat_pm |
tot_hbond_pm |
tot_NLconts_pm |
tot_nlpstat_pm |
tot_nlsurfaceE_pm |
tot_pstat_pm | Total packing of system
tot_total_charge | Total charge
tot_total_neg_charges | Total negative charges
tot_total_pos_charges | Total positive charges

## FoldX
