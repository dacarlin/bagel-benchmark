with open( 'mutant_list' ) as fn:
    mutants = fn.read().split()

with open( 'my_config.cfg', 'w' ) as fn:
    fn.write( 'command=Pssm\n2jie_renum.pdb\npositions=' )
    my_muts = [ '{}A{}'.format( m[0], m[1:-1] ) for m in mutants ] 
    fn.write( ','.join( my_muts ) + '\n' ) 
