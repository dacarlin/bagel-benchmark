#!/bin/bash
# 
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=bglbench
#SBATCH -n 1                    # Number of cores
#SBATCH -t 0-4:05              # D-HH:MM
#SBATCH --mem-per-cpu 2000

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
/share/work/rosetta/source/bin/rosetta_scripts.linuxgccrelease @flags $MUT 

