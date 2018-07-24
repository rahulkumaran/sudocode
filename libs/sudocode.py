def get_code(filename):
	return_list = []
	variables = []
	funcs = []
	func_args = 0
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".c", "w")
	code_file_ptr.write("#include <stdio.h>\n#include <stdlib.h>\n\n")
	no = 0
	for line in file_ptr:
		no+=1
		line_elem = line.split(" ")
		line_elem[-1] = line_elem[-1].replace("\n","")
		line_elem[0] = line_elem[0].lower()
		#print("\"",line_elem[0],"\"")
		#print("gap" in line_elem)
		line_of_code = ""

		if("start" in line_elem):
			line_of_code +="int main()\n{\n"

		elif(("initialise" in line_elem) and ("int" not in line_elem) and ("float" not in line_elem)):
			line_of_code += "float " + line_elem[1]  + ";"
			variables.append("float")
			line_elem[1] = (line_elem[1].split("="))[0]
			variables.append(line_elem[1])

		elif(("initialise" in line_elem) and (("int" in line_elem) or ("float" in line_elem))):
			line_of_code += line_elem[1] + " " + line_elem[2]  + ";"
			variables.append(line_elem[1])
			line_elem[2] = (line_elem[2].split("="))[0]
			variables.append(line_elem[2])

		elif(("for" in line_elem) and ("gap" not in (line_elem[-1].split("="))[0])):
			#print(line_elem[2][-1], line_elem[4])
			start_for = (line_elem[2].split("="))[-1]
			variables.append("int")
			variables.append((line_elem[2].split("="))[0])
			if(int(start_for) < int(line_elem[4])):
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " <= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "++)\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " >= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "--)\n{"


		elif(("for" in line_elem) and ("gap" in (line_elem[-1].split("="))[0])):
			start_for = (line_elem[2].split("="))[-1]
			variables.append("int")
			variables.append((line_elem[2].split("="))[0])
			if(int(start_for) < int(line_elem[4])):
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " <= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "+=" + (line_elem[-1].split("="))[-1] + ")\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + (line_elem[2].split("="))[0] + " >= " + line_elem[4] + "; " + (line_elem[2].split("="))[0] + "-=" + (line_elem[-1].split("="))[-1] + ")\n{"


		elif("print" in line_elem):
			line_of_code += "printf(\""
			for i in range(1,len(line_elem)):
				if(line_elem[i] in variables):
					index_var = variables.index(line_elem[i])
					line_of_code += "%"
					if(variables[index_var-1]=="int"):
						line_of_code += "d\\n\"," + variables[index_var]
					if(variables[index_var-1]=="float"):
						line_of_code += "f\\n\"," + variables[index_var]
					break
				else:
					if(i==len(line_elem)-1):
						line_of_code += line_elem[i] + "\\n\""
						break;
					line_of_code += line_elem[i] + " "
			line_of_code += ");"

		elif("while" in line_elem):
			line_of_code += "while(" + line_elem[-1] + ")\n{"


		elif(("endfor" in line_elem) or ("endwhile" in line_elem)):
			line_of_code += "}"
			if("endfor" in line_elem):
				variables.pop()
				variables.pop()


		elif("function" in line_elem):
			funcs.append(line_elem[1])
			return_list = line_elem
			temp = []
			#print(line_elem)
			line_of_code += line_elem[3] + " " + line_elem[1] + "("
			index_arg = line_elem.index("args")
			#print(line_of_code)
			for i in range(index_arg+1,len(line_elem), 2):
				func_args += 1
				variables.append(line_elem[i])
				variables.append(line_elem[i+1])
				if(i+1 == len(line_elem)-1):
					line_of_code += line_elem[i] + " " + line_elem[i+1] + ")\n{"
					break
				line_elem[i+1] = line_elem[i+1].replace(",","")
				line_of_code += line_elem[i] + " " + line_elem[i+1] + ","

			#print(func_args)
			funcs.append(func_args)

			'''temp = list(line_of_code)
			temp[-1] = ")\n{"
			line_of_code = "".join(temp)'''


		elif(("return" in line_elem) and ("print" not in line_elem)):
			line_of_code = "return"
			for i in range(1,len(variables),2):
				variables[i] = (variables[i].split(","))[0]
			if(line_elem[1] in variables):
				index_return = variables.index(line_elem[1])
				if(variables[index_return-1] == return_list[3]):
					line_of_code += " " + variables[index_return]
				else:
					raise("the return type in function definition and variable type of returned value don't match!")
			line_of_code += ";\n"


		elif("endfunction" in line_elem):
			i=1
			while(i<=func_args):
				variables.pop()
				variables.pop()
				i += 1
			line_of_code += "}"
			return_list = []

		elif("call" in line_elem):
			num_values = 0
			if(line_elem[1] in funcs):
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
			print(num_values)

		elif("" == line_elem[0]):
			code_file_ptr.write("\n")
			continue
		else:
			line = line.replace("\n","")
			line_of_code += line + ";"

		code_file_ptr.write(line_of_code+'\n')

		print(variables)
		print(funcs)

	while(len(variables)>0):
		variables.pop()

	while(len(funcs)>0):
		funcs.pop()


	print(variables)

	print(funcs)
	code_file_ptr.write("}")

	code_file_ptr.close()

	







