from libs.sudocode import get_code
from libs.execute import code_execute

if(__name__=='__main__'):

	#print(__name__)
	filename = "testfiles/sudocode3.txt"

	get_code(filename)

	

	code_execute(filename[0:len(filename)-4]+".py")

	#print(__name__)


