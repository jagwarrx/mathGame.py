def getUserPoint(userName):
	#print("inside getUserPoint")
	content = []
	try:
		file = open('userScores.txt', 'r')
		
		for line in file:
			content.append(line.split())
		for sublist in content:
			if sublist[0] == userName:
				return int(sublist[1])	
		file.close()
		return -1
		
	except: 
		return -1

