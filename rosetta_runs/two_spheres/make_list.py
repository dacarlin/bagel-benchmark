from Bio.SeqUtils import IUPACData
fmt = IUPACData.protein_letters_1to3 

with open( 'mutant_list' ) as fn:
    mutants = fn.read().split()

with open( 'list', 'w' ) as fn:
    for m in mutants:
        my_flags = '-parser:script_vars target={} new_res={} -suffix _{}\n'
        my_str = my_flags.format( m[1:-1], fmt[ m[ -1 ] ].upper(), m )  
        fn.write( my_str ) 

print len( mutants ), 'mutants, submit with:' 
print 'sbatch --array=1-{} sub.sh'.format( len( mutants ) ) 