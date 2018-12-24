#print(__name__)
	
def get_code_cpp(filename):
	return_list = []		#stores the last defined function details to get return statement accordingly.
	variables = []			#Stores the list of all variables
	funcs = []		#stores list of all functions and number of args to each func
	func_args = 0		#variable to store number of args in ever function
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".cpp", "w")
	code_file_ptr.write("#include<iostream>\n\nusing namespace std;\n\n")	# adding required headers for cpp

	for line in file_ptr:
		line_elem = line.split(" ") 	# iterating all the lines in the file
		line_elem[-1] = line_elem[-1].replace("\n", "")
		line_elem[0] = line_elem[0].lower()
		line_of_code = ""

		# straing the main function
		if ("start" in line_elem):
			line_of_code += "int main() {\n"

		# initialising variables; default value is float
		elif (("initialise" in line_elem) and ("int" not in line_elem) and ("float" not in line_elem)):
			line_of_code += "float " + line_elem[1] + ';'
			variables.append("float")
			line_elem[1] = (line_elem[1].split('='))[0]
			variables.append(line_elem[1])

		elif (("initialise" in line_elem) and (("int" in line_elem) or ("float" in line_elem))):
			line_of_code += line_elem[1] + " " + line_elem[2] + ';'
			variables.append(line_elem[1])
			line_elem[2] = (line_elem[2].split('=')[0])
			variables.append(line_elem[2])

		# staring for loop with increment step size == 1	
		elif (("for" in line_elem) and ("gap" not in (line_elem[-1].split('='))[0])):
			start_for = (line_elem[2].split('='))[-1]
			variables.append('int')
			variables.append((line_elem[2].split('='))[0])
			if int(start_for) < int(line_elem[4]):
				line_of_code += 'for(int ' + line_elem[2] + '; ' + line_elem[2].split('=')[0] + ' <= ' + line_elem[4] + '; ' + line_elem[2].split('=')[0] + '++)\n{'
			else:
				line_of_code += 'for(int ' + line_elem[2] + '; ' + line_elem[2].split('=')[0] + ' <= ' + line_elem[4] + '; ' + line_elem[2].split('=')[0] + '--)\n{'
		
		# for loop if increment step is provided
		elif (('for' in line_elem) and ('gap' in (line_elem[-1].split('='))[0])):
			start_for = (line_elem[2].split('='))[-1]
			variables.append('int')
			variables.append((line_elem[2].split("="))[0])
			if int(start_for) < int(line_elem[4]):
				line_of_code += 'for(int ' + line_elem[2] + '; ' + line_elem[2].split('=')[0] + ' <= ' + line_elem[4] + '; ' + line_elem[2].split('=')[0] + '+=' + (line_elem[-1].split("="))[-1] + ')\n{'
			else:
				line_of_code += 'for(int ' + line_elem[2] + '; ' + line_elem[2].split('=')[0] + ' <= ' + line_elem[4] + '; ' + line_elem[2].split('=')[0] + '-=' + (line_elem[-1].split("="))[-1] + ')\n{'
		
		# starting while loop
		elif('while' in line_elem):
			line_of_code += 'while(' + line_elem[-1] + ') {'

		 # ending loops
		elif(('endfor' in line_elem) or ('endwhile' in line_elem)):
			line_of_code += '}'
			if('endfor' in line_elem):
				variables.pop()
				variables.pop()

		# adding if condtion
		elif(('if' in line_elem)):
			line_of_code += 'if (' + line_elem[1]+ ') {'

		# adding else condition
		elif('else' in line_elem):
			line_of_code += '}\nelse {'

		# ending conditional statements
		elif('fi' in line_elem):
			line_of_code += '}'

		# implementing the print function
		elif('print' in line_elem):
			# using cout as per c++ syntax
			line_of_code += 'cout << '
			flag = 0
			for i in range(1,len(line_elem)):
				if(line_elem[i] in variables):
					# assiging values to variables
					index_var = variables.index(line_elem[i])
					line_of_code += variables[index_var]
					# using endl for new line
					line_of_code += ' << endl;'
				else:
					# condition to check so that quotes are not repeated for all the strings
					if flag == 0:
						line_of_code += '"'
						flag = 1

					# printing strings 
					if(i==len(line_elem)-1):
						line_of_code += line_elem[i] + "\" << endl;"
						break
					line_of_code += line_elem[i] + " "

		# implementing function
		elif('function' in line_elem):
			funcs.append(line_elem[1])
			return_list = line_elem		
			temp = []
			line_of_code += line_elem[3] + ' ' + line_elem[1] + ' ('
			index_arg = line_elem.index('args')

			for i in range(index_arg+1,len(line_elem), 2):
				func_args += 1
				variables.append(line_elem[i])
				variables.append(line_elem[i+1])
				if(i+1 == len(line_elem)-1):
					line_of_code += line_elem[i] + ' ' + line_elem[i+1] + ') {'
					break
				line_elem[i+1] = line_elem[i+1].replace(',','')
				line_of_code += line_elem[i] + ' ' + line_elem[i+1] + ','

			funcs.append(func_args)

		# implementing return
		elif(('return' in line_elem) and ('print' not in line_elem)):
			line_of_code = 'return'
			for i in range(1,len(variables),2):
				variables[i] = (variables[i].split(","))[0]
			if(line_elem[1] in variables):
				index_return = variables.index(line_elem[1])
				if(variables[index_return-1] == return_list[3]):
					line_of_code += ' ' + variables[index_return]
				else:
					raise("the return type in function definition and variable type of returned value don't match!")
			line_of_code += ';\n'

		# endinh the function and popping variables
		elif('endfunction' in line_elem):
			i = 1
			var_len = len(variables)/2
			while(i<=var_len):
				variables.pop()
				variables.pop()
				i += 1
			line_of_code += '}'
			return_list = []

		# implementation for function call
		elif('call' in line_elem):
			num_values = 0
			if(line_elem[1] in funcs):
				line_of_code += line_elem[1] + '('
				index_num_args = funcs.index(line_elem[1]) + 1
				index_values = line_elem.index('values')
				
				for i in range(index_values+1,len(line_elem)):
					num_values += 1
					if(i == len(line_elem)-1):
						line_of_code += line_elem[i] + ');'
						break
					line_elem[i] = line_elem[i].replace(',', '')
					line_of_code += line_elem[i] + ','

		elif("" == line_elem[0]):
			code_file_ptr.write("\n")
			continue
		else:
			line = line.replace("\n","")
			line_of_code += line + ";"

		code_file_ptr.write(line_of_code+'\n')

	# popping the variables and functions list
	while(len(variables)>0):
		variables.pop()

	while(len(funcs)>0):
		funcs.pop()

	code_file_ptr.write("return 0;\n}")

	# closing the file pointer
	code_file_ptr.close()
	file_ptr.close()




