#reverse-madlibs-generator.py by Braden

#Lists of answers for each level of difficulty:
easy_answers=["program","interpreter","syntax","strings"]
medium_answers=["function","compare","boolean","condition"]
hard_answers=["Debugging","lists","mutation","Aliasing","Break"]

#Strings for each level of difficulty
easy_level="A computer ___1___ is a set of instructions that tell the computer what to do. A python ___2___ reads your python code in order line by line and runs it. Python has its own form of grammar which, if not used properly, will result in a ___3___ error. Variables have names that refer to a value assigned in your code, and ___4___ are peices of text."
medium_level="A ___1___ usually takes in parameters and outputs with a return. 'If', 'else', 'and', and, 'or' can be used to ___2___ values. Functions can also return the ___3___ values of True and False. A while loop will continue executing a segment of code as long as the ___4___ is true."
hard_level="___1___ is when you try to find and fix problems in your code. Using ___2___ you can store multiple elements in a single variable. List ___3___ is when you change the value of an existing list. ___4___ is when you have two ways to refer to the same object. ___5___ will stop executing the current segment of code."

#Makes sure difficulty is valid (takes an new input if it isn't), prints current level and returns the list of answers for that level
def setLevel():
	global difficulty
	while difficulty!="easy"and difficulty!="medium"and difficulty!="hard":
		print "Invalid difficulty!(Difficulties are case sensitive)"
		difficulty=raw_input("Please enter a difficulty(easy, medium, or hard):")
	print "**LEVEL UP** Difficulty set to "+difficulty
	exec("current_level="+difficulty+"_level") #exec provides an easy way to put a string into a variable's name
	exec("current_answers="+difficulty+"_answers")
	print ""
	print current_level
	return current_answers

#Takes the correct answer and blank number
#splits the level into words, and then searches that string list 
#for the current blank in the level and replaces that blank with the correct answer
#Next it joins the list of strings back into a single string
#Then finally it returns the level updated with the correct answer
def fillInBlank(answer, blank_number):
	exec("updated_level="+difficulty+"_level") #exec provides an easy way to put a string into a variable's name
	updated_level=updated_level.split()
	index=0
	blank="___"+str(blank_number-1)+"___"
	for word in updated_level:
		if word==blank:
			updated_level[index]=answer
		index+=1
	updated_level=" ".join(updated_level)
	return updateLevel(updated_level)

#Takes the current level's string updated with the correct answer and changes the global level variables to the updated string
def updateLevel(updated_level):
	global easy_level #we reference theses global variable because we are changing them with a function
	global medium_level 
	global hard_level 
	if difficulty=="easy":
		easy_level=updated_level
		return easy_level
	elif difficulty=="medium":
		medium_level=updated_level
		return medium_level
	elif difficulty=="hard":
		hard_level=updated_level
		return hard_level

#Loops through the current level's answers to check if the user's inputed answers are correct
#if the answer is correct this function fills in the blank with the correct answer then
#moves on to the next blank and answer
#If the answer is incorrect it let's the user know so that they submit a correct answer
def getAndCheckAnswers(current_answers):
	blank_number=1
	while blank_number<=len(current_answers):
		blank_number_string=str(blank_number)
		print ""
		answer=raw_input("What goes in blank number "+blank_number_string+"? ")
		if answer==current_answers[blank_number-1]:
			blank_number+=1
			print "**CORRECT**"
			print ""
			print fillInBlank(answer, blank_number)
		else:
			print "**INCORRECT** (Answers are case sensitive)('Ctrl+C' to quit)" 

#checks the current difficulty and set's it to the next hardest and then initiates the next level 
#but if the difficulty is already hard there is no harder difficulty so it congratulates the player for winning
def nextLevel():
	global difficulty #we reference this global variable because we are changing it with a function
	if difficulty=="easy":
		difficulty="medium"
		getAndCheckAnswers(setLevel())
	elif difficulty=="medium":
		difficulty="hard"
		getAndCheckAnswers(setLevel())
	elif difficulty=="hard":
		print ""
		print "*...:::Congratulations, you won!:::...*"
	
print "...:::Welcome to Braden's Madlibs Game:::..."
print ""
difficulty=raw_input("Please enter a difficulty(easy, medium, or hard):")#Player sets difficulty
getAndCheckAnswers(setLevel())#Game starts
while difficulty!="hard":#this will load the next level as long as the difficulty isn't hard
	nextLevel()
nextLevel()#if the interpreter gets this far then the difficulty must be hard and the player must have finished the game