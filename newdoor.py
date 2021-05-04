#!/usr/bin/env python
import sys
import requests


#arguments should be things like cookies or IDs to use in a request
#last arguments should be a text file with the urls


if len(sys.argv) > 3:
	ID= sys.argv[1]
	cookie=sys.argv[2]
	
	#read the text file
	f = open(sys.argv[3],"r")
	line = f.readline().strip("\n")
	for line in f:
		response = requests.get('https://api.github.com')
		params={'id': ID,'cookie',cookie}
		print(line,response.status_code,ID,cookie)
		
	f.close()
	    
    
    	
    	
