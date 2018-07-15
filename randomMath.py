import random

operandList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
operatorList = ['','','','','','','','','','','','','','','','','','','','']
operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

length_of_expression = 5

def generateQuestion(length_of_expression):
	for i in range(0, length_of_expression):
		operandList[i] = str(random.randint(1,9))
	for i in range(0, length_of_expression - 1):
		if operatorList[i-1] == "**":
			operatorList[i] = operatorDict[random.randint(1,3)]
		else:
			operatorList[i] = operatorDict[random.randint(1,4)]

	questionString = ''
	for i in range(0,length_of_expression-1):
		questionString = questionString + str(operandList[i]) + str(operatorList[i])
		if i == length_of_expression-2:
			questionString = questionString + str(operandList[i+1])
	result = eval(questionString)
	String = questionString.replace("**", "^")
	print ("Your Question is: %s")%(String)
	getAnswer(String, result)

def getAnswer(question, result):
	try:
		answer = input("Your answer please: ")
		checkAnswer(answer, question, result);
	except:
		print("You need to enter a number!")
		getAnswer(question, result)


def checkAnswer(answer, question, result):
		if(int(answer)==result):
			print("Congrats! You got it correct!")
			return 1
		else:
			print("Sorry, wrong answer! Correct answer is %d")%(result)
			return 0



generateQuestion(5)
