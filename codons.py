def create_codon_dict(file_path):
  path = "data/codons.txt"
  file = open(path)
  rows = file.readlines()
  file.close()
  codon_to_amino = {}
  for row in rows:
     cells = row.strip().split('\t')
     codon = cells[0]
     amino = cells[2]
     codon_to_amino[codon] = amino
  return codon_to_amino


