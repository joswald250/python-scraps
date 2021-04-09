class Error(Exception):
#base class for other exceptions (which will be called errors)
	pass

class blankError(Error):
#The input should not be blank
def __init__(self, *args: object):
	self.msg = "You can't leave this input blank!"
	super().__init__(*args: object)

def blankError(self, msg):
	pass
