#!/bin/bash
#
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=hybridize
#SBATCH -n 1
#SBATCH -t 0-24:00

#=$( sed -n "$SLURM_ARRAY_TASK_ID p" list )
/share/work/rosetta/source/bin/rosetta_scripts.linuxgccrelease @flags
