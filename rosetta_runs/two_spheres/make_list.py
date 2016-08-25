from Bio.SeqUtils import IUPACData
nstruct = 100  

with open( 'mutant_list' ) as fn:
    mutants = list( set ( [ i.strip() for i in fn.readlines() if len( i ) > 1 ] ) ) 

runs = [
    '-parser:script_vars target={} new_res={} -suffix _{}_{:04d}\n'.format( 
    m[1:-1], IUPACData.protein_letters_1to3[ m[-1] ].upper(), m, i ) 
    for i in range( nstruct ) for m in mutants 
]

with open( 'list', 'w' ) as fn:
    fn.write( ''.join( runs ) )


print len( mutants ), 'mutants, submit with:' 
#print 'nstruct', nstruct
#print 'writing to \'list\'' 
print 'sbatch --array=1-{} sub.sh'.format( len( mutants ) * nstruct ) 
