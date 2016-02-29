#!/bin/sh
#SBATCH --job-name=bglb
#SBATCH --output=log.txt 

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
/share/work/rosetta/source/bin/rosetta_scripts.linuxgccrelease @flags $MUT 
