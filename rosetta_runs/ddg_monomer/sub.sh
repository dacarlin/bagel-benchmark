#!/bin/bash
#
#SBATCH --job-name=ddg
#SBATCH --output=logs/slurm-%A_%a.out
#SBATCH --error=logs/slurm-%A_%a.err
#SBATCH --mem 4GB 
#SBATCH --array=1

MUT=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
module load rosetta 

cd ddg_runs 
cp -r ../run_template run_$SLURM_ARRAY_TASK_ID 
cd run_$SLURM_ARRAY_TASK_ID 

touch example_file.txt 
echo ddg_monomer.linuxgccrelease @low_res_flags $MUT 
