import random 
import os
import random

def updateUserPoints(newUser, userName, score):
	#print("inside updateUserPoints")
	if newUser==True:
		#print('Inside New User')
		file = open('userScores.txt', 'a')
		tempWrite =  str(userName) + ' ' + str(score)
		file.write(tempWrite)
		file.write('\r\n')
		file.close()
		
		# PRINTING SCORESHEET
		file = open('userScores.txt', 'r')
		print("\nSCORESHEET")
		print("--------------------")
		for line in file:
			print line
		file.close()

	else:
		file = open('userScores.txt', 'r')
		tempList = []
		tempFile = open('userScores.tmp','w')
		print("\nSCORESHEET")
		print("--------------------")
		for line in file:
			tempList.append(line.split())
		for sublist in tempList:
			if sublist[0] == userName:
				sublist[1] = score
			tempWrite = str(sublist[0]) + ' ' + str(sublist[1]) 
			print(tempWrite)
			tempFile.write('{}\r\n'.format(tempWrite))
		print("\n")
		file.close()
		tempFile.close()
		os.remove('userScores.txt')
		os.rename( 'userScores.tmp', 'userScores.txt')

# updateUserPoints(True, 'GummyBears', 25)
