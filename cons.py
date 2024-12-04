#CONS

seqs = [
"GGGCAACT", 
"ATGGATCT", 
"AAGCAACC", 
"ATCCAGCT", 
"TTGGAACT", 
"ATGCCATT", 
"ATGGCACT",
"GUCCTACU" 
]

counter = {
    "A": 0,
    "C": 0,
    "T": 0, 
    "G": 0
}


#only for position 0
#for s in seqs:
#    base = s[0][0]
#    counter[base] += 1
#counter
#{'A': 1, 'C': 0, 'T': 0, 'G': 1}


for s in seqs:
    i = 0
    j = 0
    base = seqs[i][j]
    counter[base] += 1
    j += 1
    if j == len(s):
        i += 1
        j = 0



