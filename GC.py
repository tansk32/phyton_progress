#!/usr/bin/env python

from util import read_input

fasta = read_input('./test.fasta') #whut

#dictionary (called sequences) with id and sequence
sequences = {}
current_id = ""
for line in fasta:
    if line[0] == ">":
        header = line
        print(header)
        current_id = header[1:]
        sequences[current_id] = ""
    else:
        sequence = line
        print(sequence)
        sequences[current_id] = sequences[current_id] + sequence

print(sequences)

#by processing this one we will get the key(:%) dictionary
gc_content = {}
for sew
for key in sequences
# idea: calculate #Cs, #Gs, add up, divide by length of sequence, *100
# idea: we solved this problem before! see DNA.py --> paste solution

counts = {
     'A': 0,
     'T': 0,
     'C': 0,
     'G': 0,
 }

dna = "GATTACCA"
for base in dna:
     counts[base] += 1

gc = (counts['G'] + counts['C']) / len(dna) * 100
print(gc)

# # idea: loop over dictionary, see if current value is max
 gc_content = {
     "id1": 1,
     "id3": 89,
     "id2": 56,
     "id4": 27,
 }


max_value = 0
max_id = ""
for seq_id, current_gc_value in gc_content.items():
     print(f"current max value: {max_value} current max id: {max_id}")
     print("input:", seq_id, current_gc_value)
     # is the maximum value smaller than the current value?
     if current_gc_value > max_value:
         print("input was greater than max!")
         max_value = current_gc_value
         max_id = seq_id




        
      