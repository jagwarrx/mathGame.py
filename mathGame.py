import random 
import os

from getUserPoint import getUserPoint
from getAnswer import getAnswer
from checkAnswer import checkAnswer
from updateUserPoints import updateUserPoints
from generateQuestion import generateQuestion
	#try:
name = raw_input("Please enter your name: ")
userPoints = getUserPoint(str(name))

if(userPoints == -1):
	newUser = True
	userPoints = 0
	print("Welcome, "+ str(name) +". You will embark on an exciting math adventure! Score 1 point for each correct answer.")
else:
	print("Welcome Back, " + str(name) + "! Your current score is " + str(userPoints) + " points.")
	newUser = False

level = input("Choose your level of difficulty (3-5): ")

userChoice = "Y"
while( userChoice != "N" ):
	userPoints += int(generateQuestion(level))
	userChoice = raw_input("Your score is " + str(userPoints)+ " points. Let's do another question? Enter Y/N: ")
print("Thank you for playing, " + str(name) + "!")
updateUserPoints(newUser, name, userPoints)
	#except:
		#print("Error 404")
