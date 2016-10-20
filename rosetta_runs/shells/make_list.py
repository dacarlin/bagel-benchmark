import pandas 

fmt = dict( zip( 'ANDRCQEGHILKMPFSTWYV', [
    'ALA','ASN','ASP','ARG','CYS','GLN','GLU',
    'GLY','HIS','ILE','LEU','LYS','MET','PRO','PHE','SER',
    'THR','TRP','TYR','VAL' ] ) ) 

df = pandas.read_csv( '../../data_sets/reference/distance_from_active_site.csv' )
df = df.sort_values( by='distance' ) 

with open( 'list', 'w' ) as fn:
    for m in df[ 'name' ]:
        my_flags = '-parser:script_vars target={} new_res={} -suffix _{}\n'
        my_str = my_flags.format( m[1:-1], fmt[ m[ -1 ] ].upper(), m )  
        fn.write( my_str ) 

print( len( df ), 'mutants, submit with:' ) 
print( 'sbatch --array=1-{} sub.sh'.format( len( df ) ) ) 

