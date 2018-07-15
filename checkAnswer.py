def checkAnswer(answer, question, result):
		#print("inside checkAnswer")
		if(int(answer)==result):
			print("Congrats! You got it correct!")
			return 1
		else:
			print("Sorry, wrong answer! Correct answer is %d")%(result)
			return 0



