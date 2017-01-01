import pandas 
from glob import glob 

g = glob( 'output_files/*.scored.pdb' ) 
for f in g: 
    df = pandas.read_csv( f, sep='\s+', skiprowss=, header='leader' ) 
    dfs.append( df ) 

df = pandas.concatenate( dfs ) 
df = df.groupby( 'description' ).apply( lambda x: x.sort_values( 'total_score' ).head( 10 ).mean() ) 
df.to_csv( 'feature_set.csv' ) 
