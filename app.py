if(__name__=='__main__'):
	#filename = str(input("Enter name of the file that has the pseudocode: "))
	filename = "sudocode.txt"
	file_ptr = open(filename, "r")
	code_file_ptr = open(filename[0:len(filename)-4]+".c", "w")
	code_file_ptr.write("#include <stdio.h>\n#include <stdlib.h>\nint main()\n{\n")
	for line in file_ptr:
		line_elem = line.split(" ")
		line_elem[-1] = line_elem[-1].replace("\n","")
		print(line_elem)
		print("int" in line_elem)
		line_of_code = ""
		if(("int" not in line_elem) and ("float" not in line_elem) and ("Initialise" in line)):
			line_of_code += "float " + line_elem[1]  + ";"
		if(("Initialise" in line) and (("int" in line_elem) or ("float" in line_elem))):
			line_of_code += line_elem[1] + " " + line_elem[2]  + ";"

		code_file_ptr.write(line_of_code+'\n')

	code_file_ptr.write("}")
