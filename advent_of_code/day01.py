#!/usr/bin/env python

# chief historian's office; comparing reports

from util import read_input

raw = read_input("./aoc_data/day01_test.txt")
list_a = []
list_b = []
for line in raw: 
    tmp = line.split(' ')
    a = int(tmp[0])
    b = int(tmp[-1])
    list_a.append(a)
    list_b.append(b)

#print(list_a)
#print(list_b)

#list_a.sort()
#list_b.sort()
#
#sum_of_differences = 0
#for a, b in zip(list_a, list_b):
#    diff = abs(a - b)
#    sum_of_differences += diff
#
#print(sum_of_differences)
#
##Part2
test_a = [3, 4, 9, 7, 3]
test_b = [3, 3, 4, 4, 5]

def count_occurrences(x, l):
    counter = 0
    for number in l:
        if x == number:
            counter += 1

print(count_occurrences(3, test_a))
