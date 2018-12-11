from libs.sudocode import get_code, get_code_cpp
from libs.cleaner import code_cleaner, code_execute

if(__name__=='__main__'):

	#print(__name__)
	filename = "testfiles/sudocode3.txt"

	get_code(filename)
	get_code_cpp(filename)

	code_cleaner(filename[0:len(filename)-4]+".c")
	code_cleaner(filename[0:len(filename)-4]+".cpp")

	code_execute(filename[0:len(filename)-4]+".c")

	#print(__name__)
