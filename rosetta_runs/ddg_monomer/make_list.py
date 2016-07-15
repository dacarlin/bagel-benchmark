with open( 'mutant_list' ) as fn:
  mutants = fn.read().split()

for m in mutants:
  with open( 'resfiles/{}.res'.format( m ), 'w' ) as fn:
    fn.write( '{} A PIKAA {}\n'.format( m[1:-1], m[-1] ) )

with open( 'list', 'w' ) as fn:
  my_list = [ '-resfile resfiles/{}.res\n'.format( m ) for m in mutants ] 
  fn.write( ''.join( my_list ) ) 
