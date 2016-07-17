my_str = '--aminoacids={} --positions={}'

with open( 'individual_list.txt' ) as fn: 
  mutant_list = fn.read().split() 

for x in mutant_list:
  print my_str.format( x[-1], x ) 
