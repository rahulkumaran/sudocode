from libs.sudocode import get_code
from libs.cleaner import code_cleaner, code_execute
import sys
usage="USAGE: python main.py <name_of_file>"


if(len(sys.argv)==1):
	print("Error: Too few arguments")
	print(usage)
	sys.exit(0)
elif (len(sys.argv)>2):
	print("Error: Too many arguments")
	print(usage)
	sys.exit(0)

if(__name__=='__main__'):

	#print(__name__)
	filename = sys.argv[1]

	get_code(filename)

	code_cleaner(filename[0:len(filename)-4]+".c")

	code_execute(filename[0:len(filename)-4]+".c")

	#print(__name__)
