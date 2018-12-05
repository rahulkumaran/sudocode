#print(__name__)


def variable_line(line_elem):
		
		''' Uncomment to test the function 
		
		line_elem = line_elem.split(" ")	#tokenisation at space
		line_elem[-1] = line_elem[-1].replace("\n","")	#replacing new line char with null char
		line_elem[0] = line_elem[0].lower()	
		line_elem=list(filter(lambda x: x!='', line_elem))
		'''

		elem_no=0               #the index of the word in the line we are probing
		var_type="" 			#the type of variable
		var_value=''			#the value of variable
		var_identifier=""		#variable indentifier
		if(line_elem[elem_no] in ["int", "float", "char"]): #check if there is a type specified
			var_type=line_elem[elem_no] #assign the type
			elem_no+=1					#increment elem_no i.e. to probe the next element
			if(var_type=="int"):
				var_value="0"
			elif(var_type=="float"):
				var_value="0.0"
			else:
				var_value="\'\'"		#Assigning default values in case no defined value is found

		else: 							#check if the data type is alpha or numeric
			if(line_elem[-1][-1]=='\''):
				var_type="char"
				var_value="\'\'"
			else:
				var_type="float"
				var_value="0.0"


		#if there is an equal to, separate the identifier and value
		
		#CASES TO BE DEALT WITH:
		#	<indentifier><equal to><value>
		#	<identifier><space><equal to><value>
		#	<identifier><space><equal to><space><value>
		#	<identifier><equal to><space><value>
			
		
		
		if('=' in line_elem[elem_no]):   
			pos=line_elem[elem_no].find("=")
			var_identifier=line_elem[elem_no][0:pos]
			line_elem[elem_no]=line_elem[elem_no][pos:]

		else:
			var_identifier=line_elem[elem_no]
			elem_no+=1

		#print(len(line_elem))

		#checking if there is a value assigned or not. If it is assign it.

		if(elem_no<len(line_elem)):
			if(line_elem[elem_no]=="="):
				var_value=line_elem[elem_no+1]

			elif (line_elem[elem_no][0]=="="):
				var_value=line_elem[elem_no][1:]

		return (var_type, var_identifier, var_value)



def get_code(filename):
	return_list = []		#stores the last defined function details to get return statement accordingly.
	variables = []			#Stores the list of all variables
	funcs = []		#stores list of all functions and number of args to each func
	func_args = 0		#variable to store number of args in ever function
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".c", "w")
	code_file_ptr.write("#include <stdio.h>\n#include <stdlib.h>\n\n")
	no = 0
	
	





	for line in file_ptr:		#going through every line

		no+=1		#incrementing line count
		line_elem = line.split(" ")	#tokenisation at space
		line_elem[-1] = line_elem[-1].replace("\n","")	#replacing new line char with null char
		line_elem[0] = line_elem[0].lower()	#converting the first word in list_elem to all lower case letters
		
		#print("\"",line_elem[0],"\"")
		#print("gap" in line_elem)
		line_of_code = ""	#initialising var to get the final line of code to be inserted in file

		if("start" in line_elem):		#start keyword starts main function
			line_of_code +="int main()\n{\n"

		elif "initialise" in line_elem:

			line_elem=list(filter(lambda x: x!='', line_elem)) #filter out excessive spaces
			var_type, var_identifier, var_value=variable_line(line_elem[1:]) #send the line to function except the word 'initialise' as it has been processed once
			
			variables.append(var_type)
			variables.append(var_identifier)
			line_of_code=var_type+" "+var_identifier+"="+var_value+";"
			'''
			elif(("initialise" in line_elem) and ("int" not in line_elem) and ("float" not in line_elem)):
				line_of_code += "float " + line_elem[1]  + ";"	#default type is float
				variables.append("float")		#storing var type in stack
				line_elem[1] = (line_elem[1].split("="))[0]	#need to store var name so tokenising at = in order to get name of var
				variables.append(line_elem[1])		#pushing var name into variables stack

			elif(("initialise" in line_elem) and (("int" in line_elem) or ("float" in line_elem))):
				line_of_code += line_elem[1] + " " + line_elem[2]  + ";"
				variables.append(line_elem[1])		#storing var type in stack

				#spacing issues

				line_elem[2] = (line_elem[2].split("="))[0]	#need to store var name so tokenising at = in order to get name of var
				variables.append(line_elem[2])		#pushing var name into variables stack
			'''
		elif(("for" in line_elem) and ("gap" not in (line_elem[-1].split("="))[0])):	#by default gap is 1 and since gap is not in line_elem, it'll be considered at 1 only.
			#print(line_elem[2][-1], line_elem[4])
			start_for = (line_elem[2].split("="))[-1]	#tokenising at = to understand what the start value is
			variables.append("int")		#appending the type int to variables stack as we're assuming that the looping var is a newly defined temp one
			variables.append((line_elem[2].split("="))[0])	#tokenising at = to know what the var name is to push into stack
			if(int(start_for) < int(line_elem[4])):		#check to see whether loop is incrementing loop or decrementing loop
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " <= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "++)\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " >= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "--)\n{"


		elif(("for" in line_elem) and ("gap" in (line_elem[-1].split("="))[0])):	#since gap is mentioned, the jumps of looping variable must be changed
			start_for = (line_elem[2].split("="))[-1]	#tokenising at = to understand what the start value is
			variables.append("int")		#appending the type int to variables stack as we're assuming that the looping var is a newly defined temp one
			variables.append((line_elem[2].split("="))[0])	#tokenising at = to know what the var name is to push into stack
			if(int(start_for) < int(line_elem[4])):		#check to see whether loop is incrementing loop or decrementing loop
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " <= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "+=" + (line_elem[-1].split("="))[-1] + ")\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " >= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "-=" + (line_elem[-1].split("="))[-1] + ")\n{"


		elif("while" in line_elem):	#check if while loop implementation
			line_of_code += "while(" + line_elem[-1] + ")\n{"	#condition added in while


		elif(("endfor" in line_elem) or ("endwhile" in line_elem)):	#checking if for or while loop is ending
			line_of_code += "}"
			if("endfor" in line_elem):	#if for loop ending, pop out last 2 values as they are temp var type and name
				variables.pop()
				variables.pop()

		elif(("if" in line_elem)):
			line_of_code += "if(" + line_elem[1]+ ")\n{"
		elif("else" in line_elem):
			line_of_code += "}\nelse\n{"

		elif("fi" in line_elem):
			line_of_code += "}"

		elif("print" in line_elem):		#print function implementation
			line_of_code += "printf(\""
			for i in range(1,len(line_elem)):	#getting each word to be printed
				if(line_elem[i] in variables):		#checking if print statement is referring to variables being printed
					index_var = variables.index(line_elem[i])	#get index of that particular variable
					line_of_code += "%"
					if(variables[index_var-1]=="int"):	#checking one index before the var name to check var type in order to get right format specifier
						line_of_code += "d\\n\"," + variables[index_var]
					if(variables[index_var-1]=="float"):
						line_of_code += "f\\n\"," + variables[index_var]
					break
				else:
					if(i==len(line_elem)-1):	#check if last word of string is being printed
						line_of_code += line_elem[i] + "\\n\""	#adding \n char for new line
						break
					line_of_code += line_elem[i] + " "	#spacing need for each word
			line_of_code += ");"


		elif("function" in line_elem):		#check for functions part
			funcs.append(line_elem[1])	#adding func name to funcs stack
			return_list = line_elem		#storing the line_elem list vals in return_list to get return type
			temp = []
			#print(line_elem)
			line_of_code += line_elem[3] + " " + line_elem[1] + "("	#func defn
			index_arg = line_elem.index("args")	#check where args is indexed
			#print(line_of_code)
			for i in range(index_arg+1,len(line_elem), 2):	#start going through list in gaps of 2 to get var type and name
				func_args += 1	#incrementing the func_args by 1 
				variables.append(line_elem[i])	#pushing args to variables list for checking return value validity
				variables.append(line_elem[i+1])
				if(i+1 == len(line_elem)-1):
					line_of_code += line_elem[i] + " " + line_elem[i+1] + ")\n{"
					break
				line_elem[i+1] = line_elem[i+1].replace(",","")
				line_of_code += line_elem[i] + " " + line_elem[i+1] + ","

			#print(func_args)
			funcs.append(func_args)	#appending number of args to stack

			'''temp = list(line_of_code)
			temp[-1] = ")\n{"
			line_of_code = "".join(temp)'''


		elif(("return" in line_elem) and ("print" not in line_elem)):	#check for return statement
			line_of_code = "return"
			for i in range(1,len(variables),2):	#jumping through 2 in number to remove the commas at the end
				variables[i] = (variables[i].split(","))[0]
			if(line_elem[1] in variables):	#check if return var in variables stack
				index_return = variables.index(line_elem[1])	#getting index of return var name
				if(variables[index_return-1] == return_list[3]):	#checking types are same or not
					line_of_code += " " + variables[index_return]	#then adding to line_of_code
				else:
					raise("the return type in function definition and variable type of returned value don't match!")
			line_of_code += ";\n"


		elif("endfunction" in line_elem):	#endfunction keyword check
			i=1
			var_len = len(variables)/2
			while(i<=var_len):	#popping out all function arg vars
				variables.pop()
				variables.pop()
				i += 1
			line_of_code += "}"
			return_list = []	#return list set to empty

		elif("call" in line_elem):	#to call functions in main
			num_values = 0
			if(line_elem[1] in funcs):	#checking if func name is funcs stack
				line_of_code += line_elem[1] + "("
				index_num_args = funcs.index(line_elem[1]) + 1
				index_values = line_elem.index("values")
				
				for i in range(index_values+1,len(line_elem)):
					num_values += 1
					if(i == len(line_elem)-1):
						line_of_code += line_elem[i] + ");"
						break
					line_elem[i] = line_elem[i].replace(",","")
					line_of_code += line_elem[i] + ","
			#print(num_values)

		elif("" == line_elem[0]):	#if nothing exists then leave line
			code_file_ptr.write("\n")
			continue
		else:		#for normal statements like adding and all.
			line = line.replace("\n","")
			line_of_code += line + ";"

		code_file_ptr.write(line_of_code+'\n')	#writing line of code into file

		#print(variables)
		#print(funcs)

	while(len(variables)>0):	#popping out all variables type and name
		variables.pop()

	while(len(funcs)>0):	#popping out all func names and no. of args
		funcs.pop()


	#print(variables)

	#print(funcs)
	code_file_ptr.write("}")	#ending the code with a last }

	code_file_ptr.close()	#closing code file ptr.
	file_ptr.close()	#closing file ptr 

''' Testing

print(variable_line("x='A'"))
print(variable_line("x"))
print(variable_line("char a='a'"))
print(variable_line("int x =312"))
print(variable_line("int x= 312"))
print(variable_line("int x = 312"))
print(variable_line("int  x   =    312"))
print(variable_line("int x=123"))
'''





