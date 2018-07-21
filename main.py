from libs.sudocode import get_code
from libs.cleaner import code_cleaner, code_execute

if(__name__=='__main__'):
	
	filename = "sudocode2.txt"

	get_code(filename)

	code_cleaner(filename[0:len(filename)-4]+".c")

	code_execute(filename[0:len(filename)-4]+".c")
