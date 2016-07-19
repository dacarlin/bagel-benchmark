with open( 'mutant_list' ) as fn:
  mutants = fn.read().split()

for m in mutants:
  with open( 'mut_files/{}.mut'.format( m ), 'w' ) as fn:
    fn.write( 'total 1\n1\n{} {} {}\n'.format( m[0], m[1:-1], m[-1] ) )

with open( 'list', 'w' ) as fn:
  my_list = [ '-ddg::mut_file ../../mut_files/{}.mut\n'.format( m ) for m in mutants ] 
  fn.write( ''.join( my_list ) ) 
