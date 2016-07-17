#!/bin/bash
# 
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=bglb_feat
#SBATCH -n 1
#SBATCH -t 0-1:00
#SBATCH --mem-per-cpu 2GB
##SBATCH --array=1-100 
#SBATCH --array=99

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
/share/work/rosetta/source/bin/rosetta_scripts.linuxgccrelease @flags -s $MUT 

