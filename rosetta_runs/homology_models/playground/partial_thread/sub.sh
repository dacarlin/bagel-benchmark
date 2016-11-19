#!/bin/bash
#
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --job-name=partial_thread
#SBATCH -n 1
#SBATCH -t 0-24:00

/share/work/rosetta/source/bin/partial_thread.linuxgccrelease @flags 
