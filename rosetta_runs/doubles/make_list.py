import pandas 
from itertools import combinations 

fmt = dict( zip( 'ANDRCQEGHILKMPFSTWYV', [
    'ALA','ASN','ASP','ARG','CYS','GLN','GLU',
    'GLY','HIS','ILE','LEU','LYS','MET','PRO','PHE','SER',
    'THR','TRP','TYR','VAL' ] ) ) 

df = pandas.read_csv( '../../data_sets/reference/distance_from_active_site.csv' )
df = df.sort_values( by='distance' ) 

with open( 'list', 'w' ) as fn:
    for m, n in combinations( df[ 'name' ], 2 ):
        if m[1:-1] != n[1:-1] and m[0] != m[-1] and n[0] != n[-1]: 
            my_flags = '-parser:script_vars t1={} n1={} t2={} n2={} -suffix _{}+{}\n'
            my_str = my_flags.format( m[1:-1], fmt[m[-1]], n[1:-1], fmt[n[-1]], m, n )  
            fn.write( my_str ) 

