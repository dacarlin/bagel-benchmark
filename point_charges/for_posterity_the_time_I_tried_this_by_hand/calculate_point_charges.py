class Atom():

  def __init__( self, my_string ):

    s = my_string.split()
    self.x = s[6]
    self.y = s[7]
    self.z = s[8]

    atom_charge = { 'C': 0, 'N': 1, 'O': -1 }
    my_atom_name = s[10]
   
    if my_atom_name in atom_charge.keys():
      self.charge = atom_charge[ my_atom_name ]
    else:
      self.charge = 0 


