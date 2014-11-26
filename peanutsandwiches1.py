# Peanut Butter Jelly Time!
bread=9
peanut_butter=11
jelly=0
missing_ingredient="none"



# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich
print "--FIRST GOAL--"
if bread >= 2 and peanut_butter != 0 and jelly !=0:
    print "I can make a peanut butter and jelly sandwich"
else:
    print "Looks like I don't have a lunch today"

  #-----------------------------------------------------------#  

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make
print "--SECOND GOAL--"
sandwich= bread / 2
if min(peanut_butter,jelly) > sandwich:
    print "I can make",sandwich,"sandwiches min is bigger@@@@"
    
elif min(peanut_butter,jelly)<= sandwich:
    print "I can make",min(bread,peanut_butter,jelly),"sandwiches"
else:
    print "We do not have enaugh bread"

  #-----------------------------------------------------------#
    
# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )
# for this , I will use a remainder division % 
print "--THIRD GOAL--"
if bread % 2==1 and peanut_butter %2 ==1 and jelly % 2 ==1:
     print "We can also make an open-face peanut butter jelly sandwich"
else:
    print "We have a total of ",min(bread,peanut_butter,jelly),"regular sandwiches, there is no open-face sandwich "

  #-----------------------------------------------------------#

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches
# this verifie if there is any ingredient missing
print "--FORTH GOAL--"
if min(bread,peanut_butter,jelly) != 0:
     print "We have all ingredient necessary to make a sandwich"   
else:    
    # the condition that follows determine which is missing...that is until a found the right function that would return the 0 && the name of the variable,unless I put them in a list?!!!
    if bread==0:
         missing_ingredient="bread"
         print "We are missing ingredient to make a sandwich, We will need:",missing_ingredient," in order for us to make a sandwich "
    elif peanut_butter==0:
         missing_ingredient="peanut_butter"
         print "We are missing ingredient to make a sandwich, We will need:",missing_ingredient," in order for us to make a sandwich "
    elif jelly==0:
         missing_ingredient="jelly"
         print "We are missing ingredient to make a sandwich, We will need:",missing_ingredient," in order for us to make a sandwich "
                                                                                                                                                 
                                                                              
  #-----------------------------------------------------------#

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.
print "--FIFTH GOAL--"
if missing_ingredient=="jelly":
   print "You can make a peanut butter sandwich but you should take a hard, honest look at your life."
else:
    print "*** This is the end , thank you ****"

# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
