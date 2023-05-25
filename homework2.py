#exercise 1
# Use the following list - [1,11,14,5,8,9]#
#Create a list of numbers that are less than ten using l_1 and list comprehension
#Your output should [1,5,8,9]

numbers = [1, 11, 14, 5, 8, 9]
less_than_ten = [num for num in numbers if num < 10]
print(less_than_ten)


#exercise 2
#Using list comprehension, 
# create a list of names of 4 letters or more and capitalize each name

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
new_names1 = [name.capitalize() for name in names if len(name) >=4]
print(new_names1)

##########returning corrected
  


