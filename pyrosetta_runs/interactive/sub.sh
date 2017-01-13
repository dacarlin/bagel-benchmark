#!/bin/bash
# 
#SBATCH -t 0-0:30 
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=py_bgl 
#SBATCH --array=1-209 

python protocol.py 
