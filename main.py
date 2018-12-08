from libs import sudocode_c
from libs import sudocode_py
from libs import cleaner
import sys

if(len(sys.argv) is 2):
	if(__name__=='__main__'):

		#print(__name__)
		print("In which language do you want to convert pseudo code, python or c ?")
		user_input = str(input('python or c \n'))
		filename = sys.argv[1]

		if user_input == 'c':
			sudocode_c.get_code(filename)
			cleaner.code_cleaner(filename[0:len(filename)-4]+".c")
			cleaner.code_execute(filename[0:len(filename)-4]+".c")

		if user_input == 'python':
			sudocode_py.get_code(filename)
			cleaner.code_execute(filename[0:len(filename)-4]+'.py')
			print('f')

		#print(__name__)

elif(len(sys.argv) is 1):
	print("Error : Too few arguments")
	print("Try typing $python3 main.py path/filename.txt")

elif(len(sys.argv) > 2):
	print("Error : Too many arguments")
	print("You have passed more then 1 file")
