# beginner phyton exercices

## Python Print Exercises

###Exercise 1-a, printing text ("hello World")

print("Hello World!")

### Exercise 1-b, assiging a string to a variable

my_text="hello world!"
print (my_text)

## Python Variable Exercises

### Exercise 2-a, assigning a number to a variable

glass_of_water=3
print("I drank", glass_of_water, "glasses of water today.")

###Exercise 2-b, assigning a new value to a variable

glass_of_water=3
glass_of_water=glass_of_water + 1
print(glass_of_water)

## Python Data Type Exercises

### Exercise 3-a, assigning an integer to a variable

women_stepped_on_the_moon = 0
print(women_stepped_on_moon)

### Exercise 3-b, assigning a string to a variable

my_reason_for_coding = "fun evenings."
print(my_reason_for_coding)

### Exercise 3-c, assigning a new value to a variable

global_mean_sea_level_2018=21
global_mean_sea_level_2018= "21.36"
print(global_mean_sea_level_2018)

## Python String Exercises

### Exercise 9-a, assigning a string to a variable

str="Its always darkest before dawn."
print(str)

###Exercise 9-b, creating new strings, by using frist, second, and last characters

str="It's always darkest before dawn."
ans_1= str[0]+str[1]+str[-1]
print(ans_1)

###Exercises 9-b, replacing characters

str="It's always darkest before dawn."
str = str.replace(".", "!")
print(str)

## Python Len Exercises

### Exercise 10-a, using the len() function

lst=[11, 10, 12, 101, 99, 1000, 999]
answer_1=len(lst)
print(answer_1)

### Exercise 10-b, using len() function for strings

msg="Be yourself, everyone else is taken."
msg_length=len(msg)
print(msg_length)

###Exercise 10-c, using the len() for dictionaries

dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
ans_1=len(dict)
print(ans_1)

###Exercise 11-a, sorting lists in ascending order

lst=[11, 100, 99, 1000, 999]
lst.sort()

###Exercise 11-b, sorting strings within a list in alphabetic order

lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]
lst.sort()
print(lst)
 
###Exercise 11-c, sorting lists in descending order

lst=[11, 100, 101, 999, 1001]
*lst.sort(reverse=True)*
print(lst)

##Python Pop Exercises

### Exercise 12-a, to pop the last item of a list

lst=[11, 100, 99, 1000, 999]
popped_item=lst.pop()
print(popped_item)
print(lst)

### Exercise 12-b, using the Python pop method to remove the last list item

lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]
a=lst.index("broccoli")
item=lst.pop(a)
print(lst, item)

###Exercise 12-c, Using the Pop method to save an item of being removed

GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}
italy_gdp=GDP_2018.pop("Italy")
print(GDP_2018)
print(italy_gdp, "trillion USD")



### Note: Use the scrip with Python 3.12.7
