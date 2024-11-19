#Problem
#Given: A string s of length at most 10000 letters.
#Return: The number of occurrences of each word in s, where words are separated by spaces. 
#Words are case-sensitive, and the lines in the output can be in any order.

s=
word_count = {}
for word in s.split():
    word_count[word] = word_count.get(word, 0) +1
print(word_count)
