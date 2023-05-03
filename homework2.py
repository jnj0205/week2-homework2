#exercise 1
# Use the following list - [1,11,14,5,8,9]#
#Create a list of numbers that are less than ten using l_1 and list comprehension
#Your output should [1,5,8,9]

numbers = [1,11,14,5,8,9]

for number in numbers:
    num =[]
    num.append(number)
    if number <= 10:
        print(num)






#exercise 2
#Using list comprehension, 
# create a list of names of 4 letters or more and capitalize each name

names = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']

for name in names:

    print(name.capitalize())
  



## Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
string = 'alphanumeric'
for name1 in names2:

    print(name1.capitalize(), string())