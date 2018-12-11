from libs.sudocode_c import get_code
from libs.cleaner import code_cleaner, code_execute
import sys

if(len(sys.argv) is 2):
	if(__name__=='__main__'):

		#print(__name__)
		filename = sys.argv[1]

		get_code(filename)

		code_cleaner(filename[0:len(filename)-4]+".c")

		code_execute(filename[0:len(filename)-4]+".c")

		#print(__name__)

elif(len(sys.argv) is 1):
	print("Error : Too few arguments")
	print("Try typing $python3 main.py path/filename.txt")

elif(len(sys.argv) > 2):
	print("Error : Too many arguments")
	print("You have passed more then 1 file")
