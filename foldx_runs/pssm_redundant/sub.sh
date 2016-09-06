#!/bin/bash
#
#SBATCH -n 1
#SBATCH --job-name=single_shot
#SBATCH --output=log.txt 

foldx -f config.cfg 
