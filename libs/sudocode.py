def get_code(filename):
	return_list = []
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".c", "w")
	code_file_ptr.write("#include <stdio.h>\n#include <stdlib.h>\n\n")
	no = 0
	for line in file_ptr:
		no+=1
		line_elem = line.split(" ")
		line_elem[-1] = line_elem[-1].replace("\n","")
		line_elem[0] = line_elem[0].lower()
		print("\"",line_elem[0],"\"")
		#print("gap" in line_elem)
		line_of_code = ""

		if("start" in line_elem):
			line_of_code +="int main()\n{\n"

		elif(("initialise" in line_elem) and ("int" not in line_elem) and ("float" not in line_elem)):
			line_of_code += "float " + line_elem[1]  + ";"

		elif(("initialise" in line_elem) and (("int" in line_elem) or ("float" in line_elem))):
			line_of_code += line_elem[1] + " " + line_elem[2]  + ";"

		elif(("for" in line_elem) and ("gap" not in line_elem)):
			if(int(line_elem[2][-1]) < int(line_elem[4])):
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " <= " + line_elem[4] + "; " + line_elem[2][0] + "++)\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " >= " + line_elem[4] + "; " + line_elem[2][1] + "--)\n{"


		elif(("for" in line_elem) and ("gap" in line_elem)):
			if(int(line_elem[2][-1]) < int(line_elem[4])):
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " <= " + line_elem[4] + "; " + line_elem[2][0] + "+=" + line_elem[-1][-1] + ")\n{"
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " >= " + line_elem[4] + "; " + line_elem[2][1] + "-=" + line_elem[-1][-1] + ")\n{"



		elif(("endfor" in line_elem) or ("endwhile" in line_elem)):
			line_of_code += "}"

		elif("print" in line_elem):
			line_of_code += "printf(\""
			for i in range(1,len(line_elem)):
				if(i==len(line_elem)-1):
					line_of_code += line_elem[i]
					break;
				line_of_code += line_elem[i] + " "
			line_of_code += "\\n\");"

		elif(("while" in line_elem)):
			line_of_code += "while(" + line_elem[-1] + ")\n{"


		elif("function" in line_elem):
			return_list = line_elem
			temp = []
			line = line.replace(",","")
			line_of_code += line_elem[3] + " " + line_elem[1] + "("
			index_arg = line_elem.index("args")
			print(line_of_code)
			for i in range(index_arg+1,len(line_elem), 2):
				if(i+1 == len(line_elem)-1):
					line_of_code += line_elem[i] + " " + line_elem[i+1] + ")\n{"
					break
				line_of_code += line_elem[i] + " " + line_elem[i+1] + ","

			'''temp = list(line_of_code)
			temp[-1] = ")\n{"
			line_of_code = "".join(temp)'''

			

		elif("endfunction" in line_elem):
			line_of_code = "return " + return_list[3] + ";\n}"
			return_list = []

		elif("" == line_elem[0]):
			code_file_ptr.write("\n")
			continue
		else:
			line = line.replace("\n","")
			line_of_code += line + ";"

		code_file_ptr.write(line_of_code+'\n')

	code_file_ptr.write("}")

	code_file_ptr.close()


























