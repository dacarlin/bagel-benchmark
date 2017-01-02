import pandas 
from glob import glob 

rows = []
g = glob( 'output_files/*.scored.pdb' ) 
for i, scored_pdb in enumerate( g ): 
    clean_name = scored_pdb.split( '.' )[ 0 ].split( '/' )[ 1 ]
    with open( scored_pdb ) as fn:
        lines = fn.readlines()
        pose_line = [ i[:-1].split() for i in lines if i.startswith( 'pose' ) ][0]
        pose_line[0] = clean_name
        header = [ i[:-1] for i in lines if i.startswith( 'label' ) ][ 0 ].split() 
        rows.append( tuple( pose_line ) ) 

df = pandas.DataFrame( rows, columns=header ) 
df.to_csv( 'feature_set.csv' ) 
