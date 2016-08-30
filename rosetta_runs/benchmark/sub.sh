#!/bin/bash
# 
#SBATCH -t 0-1:00
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=bglb 
#SBATCH --array=1-206 
#SBATCH -p gc128 

hostname -f 
module load rosetta 
MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
rosetta_scripts.linuxgccrelease @flags $MUT 

