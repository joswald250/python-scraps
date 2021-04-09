import urllib.request
import webbrowser
from urllib.parse import urlparse
import sys

def websearch():
	url = ''
	while True:
		user_input = str(input('What website would you like to visit?'))
		if user_input == '':
			user_input = str(input('What website would you like to visit?'))
		else:
			break


	parse = urlparse(user_input)
	scheme = parse.scheme
	netloc = parse.netloc
	path = parse.path
	params = parse.params
	query = parse.query
	fragment = parse.fragment

	'''print('scheme1: ' + scheme)
	print('netloc1: ' + netloc)
	print('path1: ' + path)
	print('params1: ' + params)
	print('query1: ' + query)
	print('fragment1: ' + fragment)'''


	#if it is google.com or youtube.com
	if (scheme == '') and (netloc == ''):
		position = path.find('.com')
		netloc = path[:position + 4]
		path = path[position + 4:]
		#print('if 1 ran')

	#if it finds no https
	if scheme.find('https') < 0:
		scheme = "https"
		#print('if 2 ran')

	# if there is no w. at all in the netloc, it places a www. at the front
	if netloc.find('w.') < 0:
		netloc = 'www.' + netloc
		#print('if 3 ran')

	#if netloc does not include a 'w.com' and does have a 'ww.' or 'w.' should replace the first 'w.' or 'ww.' with 'www.' aka ww.google.com or w.google.com
	if ((netloc.find('w.com') < 0 and netloc.find('www.') < 0 and netloc.find('ww.') >= 0) or
		(netloc.find('w.com') < 0 and netloc.find('www.') < 0 and netloc.find('w.') >= 0)):
		position = netloc.find('w.')
		netloc = 'www.' + netloc[position+2:]
		#print('if 4 ran')

	# if netloc has w.com and w. or ww., erase either instance and replace with www. aka w.flow.com
	if ((netloc.find('w.com') >= 0 and netloc.find('ww.') >= 0 and netloc.find('www.') < 0) or
		 (netloc.find('w.com') >= 0 and netloc.find('w.') >= 0 and netloc.find('www.') < 0 and (netloc.find('w.') < netloc.find('w.com')))):
		position = netloc.find('w.')
		netloc = 'www.' + netloc[position + 2:]
		#print('if 5 ran')
	# if netloc has 'w.com' but no 'www.' or 'ww.' or 'w.' it adds 'www.' aka flow.com
	elif ((netloc.find('w.com') >=0 and netloc.find('www.') < 0) or (netloc.find('w.com') >=0 and netloc.find('ww.') < 0) or
		(netloc.find('w.com') >=0 and (netloc.find('w.') > netloc.find('w.com')))):
		netloc = "www." + netloc
		#print('if 6 ran')

	if netloc.rfind('.') < (len(netloc) - 4):
		print('Please include an ending (.com, .edu, .gov, etc...) to your net location.')
		#in master program insert: return
		#print('if 7 ran')
		sys.exit()


	url = scheme + '://' + netloc + path + params + query + fragment


	'''print('scheme: ' + scheme)
	print('netloc: ' + netloc)
	print('path: ' + path)
	print('params: ' + params)
	print('query: ' + query)
	print('fragment: ' + fragment)
	print(url)'''


	#requests the actual website
	website = urllib.request.urlopen(url)
	webbrowser.open(url, new = 2)
	print('result code: ' + str(website.getcode()))

	store_data_question = str(input('Would you like to save the website data to a file? (Enter: yes or no)'))
	if store_data_question == 'yes':
		file_location_input = str(input('What would you like to name the file?'))
		website_data = website.read()
		file = open(file_location_input, 'w+')
		file.write(str(website_data))
		file.close()



'''get the result code:
OK 200
The request was fulfilled.

CREATED 201
Following a POST command, this indicates success, 
but the textual part of the response line indicates the URI by which the newly created document should be known.

Accepted 202
The request has been accepted for processing, but the processing has not been completed. 
The request may or may not eventually be acted upon, as it may be disallowed when processing actually takes place.

Partial Information 203
When received in the response to a GET command, this indicates that the returned metainformation
is not a definitive set of the object from a server with a copy of the object, but is from a private overlaid web.

No Response 204
Server has received the request but there is no information to send back, and the client should stay in the same document view. 
This is mainly to allow input for scripts without changing the document at the same time.

Bad request 400
The request had bad syntax or was inherently impossible to be satisfied.

Unauthorized 401
The parameter to this message gives a specification of authorization schemes which are acceptable. The client should retry the request with a suitable Authorization header.

PaymentRequired 402
The parameter to this message gives a specification of charging schemes acceptable. The client may retry the request with a suitable ChargeTo header.

Forbidden 403
The request is for something forbidden. Authorization will not help.

Not found 404
The server has not found anything matching the URI given

Internal Error 500
The server encountered an unexpected condition which prevented it from fulfilling the request.

Not implemented 501
The server does not support the facility required.

Service temporarily overloaded 502
The server cannot process the request due to a high load (whether HTTP servicing or other requests). 
The implication is that this is a temporary condition which maybe alleviated at other times.

Gateway timeout 503
This is equivalent to Internal Error 500, but in the case of a server which is in turn accessing some other service, 
this indicates that the respose from the other service did not return within a time that the gateway was prepared to wait. 

Moved 301
The data requested has been assigned a new URI, the change is permanent. 

Found 302
The data requested actually resides under a different URL, however, the redirection may be altered on occasion (when making links to these kinds of document, 
the browser should default to using the Udi of the redirection document, but have the option of linking to the final document) as for "Forward".'''