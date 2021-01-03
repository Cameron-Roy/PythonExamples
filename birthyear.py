'''
Author: Cameron Roy
Date : 2020/1/6
Description: Asks user for age and name, calcuates the year of birth, then gives them a greeting.
'''

#imports the date library
import datetime
now = datetime.datetime.now()

#asks user for their name
print("Hey there user, what\'s your name?")
name = input()      #sets their answer to the variables 'name'
print("How old are you?")
age = int(input())  #sets their answer to the variable 'age', but of the type INT
print("Has your birthday happened this year?\n(y or n)")
bday = input()

#If else loop to determine whether they have had a birthday this year
if (bday == "y"):
    dob = (now.year - age)
else:   
        dob = (now.year - 1 - age) #done like this, because of birthday month tomfoolery

#prints out the results of the questions
print("You were born in",dob, name)
