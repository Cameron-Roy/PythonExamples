'''
Name: Right and triangle determiner 9000
Author: Cameron Roy
Date: 2020/1/8
Description: Takes in the lengths of 3 sides of a triangle, and proceeds to determine if they can create a right angled triangle. Using the pythagorean theorem
'''
#NOTE: Hey boomer make sure to add in "Try and Effect"
#NOTE: Later Cam: No.
right = 0

print("Hey, give me 3 sides of a triangle, and I'll tell you if its right angled or not.\nSide 1: ")
s1 = float(input()) #Uses floats instead of ints so you can use decimals in it.
print("Side 2: ")
s2 = float(input())
print("Side 3: ")
s3 = float(input())

'''
This is super basic but it works, only the 'C' in the (a^2 + b^2 = c^2) equation
needs to be isolated. The numbers in the a^2 + b^2 part can be in either order. 
To check if its possible to be a right angle triangle or not, each side has to be on
the right side of the equation, and then checked to see if its equal to the other side.

'''
if ((s1*s1) + (s2*s2) == (s3*s3)):
    right = 1
elif ((s1*s1) + (s3*s3) == (s2*s2)):
    right = 1
elif ((s2*s2) + (s3+s3) == (s1*s1)):
    right = 1
else:
    right = 0
    
    #This is just here because I didn't like having 5 print statements.
if right == 1:
    print("This is a right angle triangle.")
else:
    print("This is NOT a right angle triangle.")


