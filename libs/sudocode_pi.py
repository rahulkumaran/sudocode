#print(__name__)

def get_code(filename):
	return_list = []		#stores the last defined function details to get return statement accordingly.
	variables = []			#Stores the list of all variables
	funcs = []		#stores list of all functions and number of args to each func
	func_args = 0		#variable to store number of args in ever function
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".py", "w")
	no = 0
	count=0     #to check indentation
	for line in file_ptr:								#going through every line
		no+=1		                                    #incrementing line count
		line_elem = line.split(" ")						#tokenisation at space
		line_elem[-1] = line_elem[-1].replace("\n","")	#replacing new line char with null char
		line_elem[0] = line_elem[0].lower()				#converting the first word in list_elem to all lower case letters
		#print("\"",line_elem[0],"\"")
		#print("gap" in line_elem)
		line_of_code = ""	#initialising var to get the final line of code to be inserted in file
		space= '\t'*count
		if("start" in line_elem):		#start keyword starts main function
			pass

		elif(("initialise" in line_elem)):
			line_of_code += line_elem[1]  	#initialise in the program
			if("." in line_elem[1].split("=")[1]):
				variables.append("float")		#storing var type in stack
			if("\'" in line_elem[1].split("=")[1]):
				variables.append("char")
			else:
				variables.append("int")
			line_elem[1] = (line_elem[1].split("="))[0]	#need to store var name so tokenising at = in order to get name of var
			variables.append(line_elem[1])		#pushing var name into variables stack
			

	
		code_file_ptr.write(space)
		code_file_ptr.write(line_of_code+'\n')	#writing line of code into file


	code_file_ptr.close()	#closing code file ptr.
	file_ptr.close()	#closing file ptr 
	







