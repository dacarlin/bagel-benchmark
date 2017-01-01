#!/bin/bash
# 
#SBATCH -t 0-0:05
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=pybglb 
#SBATCH --array=1 

which python 
python protocol.py 
#python features.py 
