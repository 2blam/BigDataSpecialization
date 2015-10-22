#!/usr/bin/env python
import sys

prev_tvshow = "  "                
total = 0
ignore = True

for line in sys.stdin:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a listh   

    curr_tvshow     = key_value[0]
    value_in   	    = key_value[1] 

    if curr_tvshow != prev_tvshow and prev_tvshow != "  ":
	#new item
        #if ignore is True, do nothing, reset counter
        if not ignore:
            print( "{0} {1}".format(prev_tvshow, total) )
        
        total = 0
        ignore = True

	if value_in == "ABC":
	    ignore = False
        else:
	    total = int(value_in)

    else:
	if value_in == "ABC":
	    ignore = False
	else:
	    total = total + int(value_in)
    
    prev_tvshow = curr_tvshow
    
#last item
if not ignore:
    print( "{0} {1}".format(prev_tvshow, total) )

	

