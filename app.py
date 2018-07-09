if(__name__=='__main__'):
	#filename = str(input("Enter name of the file that has the pseudocode: "))
	filename = "sudocode.txt"
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".c", "w")
	code_file_ptr.write("#include <stdio.h>\n\n#include <stdlib.h>\nint main()\n{\n")
	no = 0
	for line in file_ptr:
		no+=1
		line_elem = line.split(" ")
		line_elem[-1] = line_elem[-1].replace("\n","")
		print(line_elem)
		print("For" in line_elem)
		line_of_code = ""
		if(("Initialise" in line_elem) and ("int" not in line_elem) and ("float" not in line_elem)):
			print(no)
			line_of_code += "float " + line_elem[1]  + ";"
		if(("Initialise" in line_elem) and (("int" in line_elem) or ("float" in line_elem))):
			print(no)
			line_of_code += line_elem[1] + " " + line_elem[2]  + ";"

		if(("For" in line_elem) and ("gap" not in line_elem)):
			if(int(line_elem[2][-1]) < int(line_elem[4])):
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " <= " + line_elem[4] + "; " + line_elem[2][0] + "++)\n{"
				print(line_of_code)
			else:
				line_of_code += "for(int " + line_elem[2] + "; " + line_elem[2][0] + " >= " + line_elem[4] + "; " + line_elem[2][1] + "--)\n{"
				print(line_of_code)

		
		if("Endfor" in line):
				print(no)
				line_of_code += "}"

		if("Print" in line):
				line_of_code += "printf(\""
				for i in range(1,len(line_elem)):
					line_of_code += line_elem[i] + " "
				line_of_code += "\")"
		
		code_file_ptr.write(line_of_code+'\n')

	code_file_ptr.write("}")
