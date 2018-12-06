import os


def code_cleaner(filename):
	try:
		temp_file = filename[0:(len(filename)-2)] + "_temp.c"  # Adding the "_temp.c" to filename
		main_file_ptr = open(filename, "r")  # Creating file pointer for the main code file
		temp_file_ptr = open(temp_file, "w")	 # Creating file pointer for temp file
		count=0			# variable to keep count of the number of "{" or "}"
		count_close = 0
		count_open = 0
		for line in main_file_ptr:
			spaces = '\t'*count		# Giving count number of tabs from next line onwards
			tab_count = line.count('\t')
			line = line.replace('\t'*tab_count,'')
			if "{" in line:
				count+=1	# incrementing count whenever "{"
				count_open +=1
			if "}" in line:
				count-=1		# Decrementing count whenever "}"
				spaces = '\t'*count
				count_close +=1

			temp_file_ptr.write(spaces)	# First writing spaces into every line
			temp_file_ptr.write(line)	# Then copy contents of every line from main code

		os.remove(filename)			# Deleting main code file
		os.rename(temp_file, filename)		# Renaming the temp file with main code file


		if (count_close - count_open) > 0:    # Checking if } more than {
			print("Looks like you have more number of \"}\" somewhere")
		if (count_close - count_open) < 0:		# Checking if { more than }
			print("Looks like you have more number of \"{\" somewhere")
		return count
	except IOError:		# If wrong file name gives
		print("Sorry, but no such file exists in your current working directory")


def code_execute(filename):
	find = filename.split(".")
	if find[1] == 'c':
		compile_command = "gcc " + filename + " -o " + filename[0:(len(filename)-2)] + "_c"    # Command for compiling with gcc along with filename and executable name
		os.system(compile_command)		# Running the above command from script to compile the code
		exec_file = "./"+filename[0:(len(filename)-2)] + "_c"	# To execute file
		os.system(exec_file)
	elif(find[1] == "cpp"):
		compile_command = "gcc " + filename + " -o " + filename[0:(len(filename)-4)] + "_cpp "    # Command for compiling with gcc along with filename and executable name
		os.system(compile_command)		# Running the above command from script to compile the code
		exec_file = "./"+filename[0:(len(filename)-4)]+"_cpp"	# To execute file
		os.system(exec_file)
	else:
		print("Sorry, but can't execute the your " + find[1] + " code mate! :(")

