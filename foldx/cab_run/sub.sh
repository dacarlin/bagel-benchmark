#!/bin/bash
#
#SBATCH -n 1
#SBATCH --output=log.txt
#SBATCH --array=1

S=$( sed -n "$SLURM_ARRAY_TASK_ID p" list ) 
cd out
cp -r ../template_dir $SLURM_ARRAY_TASK_ID
cd $SLURM_ARRAY_TASK_ID
pwd 
foldx --rotabaseLocation="/home/carlin/bin/rotabase.txt" --command=Pssm --pdb="../../2jie_renum.pdb" $S
