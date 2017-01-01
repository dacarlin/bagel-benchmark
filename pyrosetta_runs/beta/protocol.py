
# coding: utf-8

# In[1]:

import pyrosetta 
import rosetta 
from sys import argv
import os 
#os.environ[ "SLURM_ARRAY_TASK_ID" ] = "96" # for testing! 


# In[2]:

with open( '../../mutant_list.txt' ) as fn:
    mutant_list = fn.read().split()
    mutant_name = mutant_list[ int( os.environ[ 'SLURM_ARRAY_TASK_ID' ] ) - 1 ] 


# In[3]:

fmt = dict( zip( 'ANDRCQEGHILKMPFSTWYV', [
    'ALA','ASN','ASP','ARG','CYS','GLN','GLU',
    'GLY','HIS','ILE','LEU','LYS','MET','PRO','PHE','SER',
    'THR','TRP','TYR','VAL' ] ) ) 


# In[4]:

# flags from command line 
with open( 'input_files/flags' ) as fn:
    flags = fn.read().replace( '\n', ' ' )
pyrosetta.init( ''.join( flags ) ) 

# extra residue (pNPG) params 
ligand_params = pyrosetta.Vector1( [ 'input_files/pNPG.params' ] )
new_res_set = pyrosetta.generate_nonstandard_residue_set( ligand_params )

# construct pose 
p = pyrosetta.Pose()
pyrosetta.pose_from_file( p, new_res_set, 'input_files/bglb.pdb' ) 

# construct score function 
scorefxn = pyrosetta.create_score_function( 'beta_cst' ) 

# add in enzyme design constraints 
add_cst = rosetta.protocols.enzdes.AddOrRemoveMatchCsts()
add_cst.cstfile( 'input_files/pNPG.enzdes.cst' ) 
add_cst.set_cst_action( rosetta.protocols.enzdes.CstAction.ADD_NEW )
add_cst.apply( p ) 

# mutate the residue 
target = int( mutant_name[ 1:-1 ] )
new_res = fmt[ mutant_name[ -1 ] ] 
mut = rosetta.protocols.simple_moves.MutateResidue( target, new_res )
mut.apply( p ) 


# In[8]:

# set up pack task 
tf = rosetta.core.pack.task.TaskFactory()
around = rosetta.protocols.toolbox.task_operations.DesignAroundOperation()
around.include_residue( 446 ) #ligand 
around.include_residue( target ) 
around.repack_shell( 20 ) # let's grid search this  
around.resnums_allow_design( False )
around.allow_design( False )
tf.push_back( around ) 
pt = tf.create_task_and_apply_taskoperations(p)
print( pt )

# repack and minimize 
repack = rosetta.protocols.enzdes.EnzRepackMinimize()
repack.set_scorefxn_repack( scorefxn )
repack.set_scorefxn_minimize( scorefxn )
repack.set_min_bb( True )
repack.set_min_lig( True )  
repack.set_min_rb( True ) 
repack.set_min_sc( True )
repack.task_factory( tf ) # adds packer task 

# monte carlo 
parsed = rosetta.protocols.simple_moves.GenericMonteCarloMover()
parsed.set_mover( repack )
parsed.set_maxtrials( 10 )
parsed.set_scorefxn( scorefxn )
parsed.apply( p ) 

jd = pyrosetta.PyJobDistributor( p, scorefxn, nstruct=1 ) 
jd.output_scored_pdb( 'output_files/{}.scored.pdb'.format( mutant_name)  ) 

