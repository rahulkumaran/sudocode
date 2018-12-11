import os
import subprocess

def code_execute(filename):
	find = filename.split(".")
	#print(find)
	if(find[1] == 'py'):
		compile_command = "python " + filename #Command for compiling the file along with filename and executable name
		os.system(compile_command)		#Running the above command from script to compile the code
		
	
	else:
		print("Sorry, but can't execute the your " + find[1] + " code mate! :(")

