# Python program to read 
# json file 

import json 


# Opening JSON file 
f = json.load(open('/home/order/aktueller-kurs/tag_3/config.json')) 

# returns JSON object as 
# a dictionary 
data = json.load(f) 

# Iterating through the json 
# list 
for i in data['emp_details']: 
	print(i) 

# Closing file 
f.close() 
