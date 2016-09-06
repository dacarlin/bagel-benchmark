#!/bin/bash
#
#SBATCH -n 1
#SBATCH --job-name=bglb_foldx
#SBATCH --output=log.txt 

foldx -f config.cfg 
