
#Problem
#Given: A string s of length at most 200 letters and four integers a, b, c and d.
#Return: The slice of this string from indices a through b and c through d
#(with space in between), inclusively. In other words, we should include elements s[b]
#and s[d] in our slice.

s = "6inaAAyF8bNbSTN8SOQu2WkKBpmChrysopeleaHXB11KmZa2KaQn0ltX9YobFaODDuSTxiuVOOSVj8ii1lncRacggkalpinusHiNqfnkf7PFyjLi7kh7GhbCr5yIEUElp1sarwfLWlrLl9tI3TOaN1HxwogPCoDPBSfmC5R7bfqyz2."
print(s[27:37+1] + s[90:36+1])

#Output: Chrysopelea
