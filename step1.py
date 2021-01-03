'''
Program: Lesson 16: Step 1
Author: Cameron Roy
Date: 2020/05/22
Description: States a problem that can be solved with FileIO
then basic code is written without that fileIO
'''

'''
Problem: Recipie for pancakes is missing.
Needs the ingredients and then the steps, and temperature for the 
cooking element. There is also a review system, where you can give it 
a rating from 1 to 5 stars. 1 being inedible, 5 being delicious.
( Please don't actually make this recipe I made it up)
'''

print("Instructions: type \'h\' or \'help\' for help")
# Infinite while loop so it doesnt just quit out after one step.
while True:
    
    # Help menu to display how to give the program its input
    def hellp():
        print("Type \'t\' or \'temp\' for the temperature of stove or oven") 
        print("Type \'i\' or \'ingre\' for the list of ingredients")
        print("Type \'s\' or \'steps\' for the steps")
        print("Type \'r\' or \'rate\' to rate the recipe")
        print("Type \'h\' or \'help\' for this menu")

    # Prints out the ingredients used in the recipie.
    def ingredients():
         print("Ingredients:\n\t 2 cups flour\n\t 1 egg\n\t 2 teaspoons salt\n\t 2 tablespoons sugar\n\t 3 cups milk")

    # Prints out the steps for the recipie
    def steps():
        print("Mix the dry ingredients together, the flour, salt and sugar")
        print("Make a hole in the center of the mixture, and pour in the milk and egg")
        print("Mix throughly until firm and a uniform colour.")

    # Prints out the temperature of the cooking medium (In this case the stove)
    def temp():
        print("Temperature should be medium")
        print("Cook until bubbles on top have popped, then flip\n")

    # Mediocre rating system. Because it can't actually save the rating to the file,
    # this "rating" doesn't actually do anything, it only is active while the program
    # is running. For this to make sense and work, it would need to save the value to 
    # a file, that can then be referenced back to in the future to see what the recipie
    # was rated as.
    def rating():
        # Sets it as a temporary value for the star rating
        starsT = int(input("How many stars would you rate this? (1 to 5): "))
        # This catches whether the given rating is within the right range.
        # If it is, it is then stored in the final value of starsF. Here is where
        # the final rating would be saved to the file for future reference.
        if (int(starsT) <= 5 and int(starsT) >= 0):
            starsF = starsT
        # Catches if its an invalid rating
        else:
            print("Rating out of proper range")
            starsT = input("Please give a valid rating (1 to 5): ")


    # Because python is goofy and doesn't have a switch statement like every
    # other language I know, I had to find a way to create one using a function and
    # a dictionary (dictionaries are way more usefull than I originally thought)
    def userValued(x):
        # If the argument passed to user defined is one of the valid dicionary
        # things, it will run the function associted to the abbreviation.
        switcher = {
                "h": hellp,
                "help": hellp,
                "i": ingredients,
                "ingre": ingredients,
                "s": steps,
                "steps": steps,
                "t": temp,
                "temp": temp,
                "r": rating,
                "rate": rating
            }
        func = switcher.get(x,lambda: "Invalid Command")
        return func()

    # Takes user input and runs it through the function / switch statement.
    userValued(str(input()))
