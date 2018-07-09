from app import get_code
from cleaner import code_cleaner

if(__name__=='__main__'):
	
	filename = "sudocode.txt"

	get_code(filename)

	code_cleaner(filename[0:len(filename)-4]+".c")
