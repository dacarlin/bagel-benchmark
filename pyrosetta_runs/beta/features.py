import pyrosetta 
import rosetta 

# input 
with open( 'input_files/features.flags' ) as fn:
    flags = fn.read().replace( '\n', ' ' )

pyrosetta.init( ''.join( flags ) ) 

ligand_params = pyrosetta.Vector1( [ 'input_files/pNPG.params' ] )
new_res_set = pyrosetta.generate_nonstandard_residue_set( ligand_params )

p = pyrosetta.Pose()
pyrosetta.pose_from_file( p, new_res_set, 'output_files/H178K.pdb' ) 
scorefxn = pyrosetta.create_score_function( 'beta_cst' ) 

report = rosetta.protocols.features.ReportToDB()
report.add_features_reporter( rosetta.protocols.features.JobDataFeatures() ) 
#report.add_features_reporter( rosetta.protocols.features.StructureScoresFeatures( scorefxn ) ) 
report.apply( p ) 

