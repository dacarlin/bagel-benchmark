#!/bin/bash
# 
#SBATCH -t 0-15:00
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=bgl_all
#SBATCH --array=1-8880 
#SBATCH -p gc128 

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
module load rosetta 
rosetta_scripts.linuxgccrelease @flags $MUT 

