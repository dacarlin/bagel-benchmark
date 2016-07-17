from Bio.SeqUtils import IUPACData
nstruct = 100  

with open( 'mutant_list.txt' ) as fn:
    #mutants = [ i.strip() for i in fn.readlines() if len( i ) > 1 ] 
    mutants = fn.read().split()
    print len( mutants ), 'mutants'

nstruct = 100

runs = [
    '-parser:script_vars target={} new_res={} -suffix _{}_{:04d}\n'.format( 
    m[1:-1], IUPACData.protein_letters_1to3[ m[-1] ].upper(), m, i ) 
    for i in range( nstruct ) for m in mutants 
]

with open( 'list', 'w' ) as fn:
    fn.write( ''.join( runs ) )
