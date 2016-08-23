#!/bin/bash
# 
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=bglb_MD
#SBATCH -t 0-24:00
#SBATCH --mem-per-cpu 4GB 
#SBATCH --array=1

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags $MUT 

