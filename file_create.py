
fname = "./filenames"
lines = [line.strip() for line in open(fname)]

for line in lines:

  with open(line+'.xyo', 'w') as fout:
    fout.write('')
