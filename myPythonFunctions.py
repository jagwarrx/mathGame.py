import random 
import os

content = []

def getUserPoint(userName):
	try:
		file = open('userScores.txt', 'r')
		
		for line in file:
			content.append(line.split())

		for sublist in content:
			if sublist[0] == userName:
				return sublist[1]
		file.close()

	except IOError: 
		print("File Not Found.")
		file = open('userScores.txt', 'w')
		file.close()
		return "-1"

def updateUserPoints(newUser, userName, score):
	if newUser==True:
		print('Inside New User')
		file = open('userScores.txt', 'a')
		tempWrite =  str(userName) + ' ' + str(score)
		file.write(tempWrite)
		file.write('\r\n')
		file.close()
	else:
		file = open('userScores.txt', 'r')
		tempList = []
		tempFile = open('userScores.tmp','w')
		for line in file:
			tempList.append(line.split())
		for sublist in tempList:
			if sublist[0] == userName:
				sublist[1] = score
			tempWrite = str(sublist[0]) + ' ' + str(sublist[1]) 
			print(tempWrite)
			tempFile.write('{}\r\n'.format(tempWrite))
		file.close()
		tempFile.close()
		os.remove('userScores.txt')
		os.rename( 'userScores.tmp', 'userScores.txt')
		#if os.path.isfile('userScores.txt'):
		#	
		#

updateUserPoints(True, 'GummyBear', 25)


