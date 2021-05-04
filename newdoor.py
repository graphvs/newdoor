#!/usr/bin/env python
import sys

#arguments should be things like cookies or IDs to use in a request
#last arguments should be a text file with the urls
ID= sys.argv[0]
cookie=sys.argv[1]

	
#read the text file
f = open(sys.argv[2],"r")
    contents = f.read()
    f.close()
    print(ID,cookie,contents)
    
    	
    	
