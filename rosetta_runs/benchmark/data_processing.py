import pandas 
from glob import glob 

# first, let's collect all the Rosetta scorefiles into a DataFrame object 

sfs = [ pandas.read_csv( sf, sep='\s+' ) for sf in glob( 'out/*sc' ) ] 
sf = pandas.concat( sfs ) 

# we'll tidy up and then export to CSV 
sf.description = sf.description.str.split( '_' ).str[ 1 ] 
sf.set_index( 'description', drop=True, inplace=True )

sf.to_csv( 'benchmark_feature_set.csv' ) 