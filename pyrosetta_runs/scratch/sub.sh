#!/bin/bash 
#
#SBATCH --array=1-220 

python protocol.py 
