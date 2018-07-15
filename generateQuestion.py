import random
from getAnswer import getAnswer

def generateQuestion(length_of_expression):
	print("inside generateQuestion")
	operandList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	operatorList = ['','','','','','','','','','','','','','','','','','','','']
	operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}
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
	if(result > 50 or result < -50):
		point = generateQuestion(length_of_expression)
		return point
	else:
		String = questionString.replace("**", "^")
		print ("Your Question is: %s")%(String)
		point = int(getAnswer(String, result))
		return point

