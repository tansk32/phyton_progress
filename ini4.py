#Problem
#Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.

numbers = list(range(a, b+1))

odd_numbers = []
for odd in numbers:
     if odd % 2 == 1:
             odd_numbers.append(odd)

sum(odd_numbers)
 
