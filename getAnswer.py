from checkAnswer import checkAnswer

def getAnswer(question, result):
	#print("inside getAnswer")
	#try:
	answer = input("Your answer please: ")
	point = int(checkAnswer(answer, question, result))
	print("You scored " + str(point) + " points")
	return int(point)
	#except:
	#	print("You need to enter a number!")
	#	getAnswer(question, result)


