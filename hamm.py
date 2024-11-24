#HAMM
#go over both strings simulaneously, compare them,
#if diffrent add to counter
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

counter = 0
i = 0
for i in range(len(s)):
    if s[i] != t[i]:
        counter += 1
    i += 1
