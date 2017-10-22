def readFromConfig():
	config = {}
	with open('config.txt','r') as f:
	    for line in f:
	        if line[0] != '#':
	          (key,sep,val) = line.partition('=')
	          # if the line does not contain '=', it is invalid and hence ignored
	          if len(sep) != 0:
	              val = val.strip()
	              config[key.strip()] = int(val) if str.isdecimal(val) else val
	workload =  config.get('workload['+str(0+2)+']')
	workload = workload.split(';')
	operations = []
	for i in range(0,len(workload)):
		item = workload[i]
		print(item)
		#print("put" in item)
		operation_dict = {}
		if "put" in item :
			first_occur = item.find("'")
			#print(first_occur)
			second_occur = item.find("'",first_occur+1)
			#print(second_occur)
			key = item[first_occur+1:second_occur]
			first_occur = item.find("'",second_occur+1)
			second_occur = item.find("'",first_occur+1)
			value = item[first_occur+1:second_occur]
			operation_dict["operation"] = "put"
			operation_dict["key"]=key
			operation_dict["value"]=value
		elif "append" in item:
			first_occur = item.find("'")
			#print(first_occur)
			second_occur = item.find("'",first_occur+1)
			#print(second_occur)
			key = item[first_occur+1:second_occur]
			first_occur = item.find("'",second_occur+1)
			second_occur = item.find("'",first_occur+1)
			value = item[first_occur+1:second_occur]
			operation_dict["operation"] = "append"
			operation_dict["key"]=key
			operation_dict["value"]=value
		elif "slice" in item:
			first_occur = item.find("'")
			#print(first_occur)
			second_occur = item.find("'",first_occur+1)
			#print(second_occur)
			key = item[first_occur+1:second_occur]
			first_occur = item.find("'",second_occur+1)
			second_occur = item.find("'",first_occur+1)
			value = item[first_occur+1:second_occur]
			operation_dict["operation"] = "slice"
			operation_dict["key"]=key
			operation_dict["value"]=value
		elif "get" in item:	
			first_occur = item.find("'")
			#print(first_occur)
			second_occur = item.find("'",first_occur+1)
			#print(second_occur)
			key = item[first_occur+1:second_occur]
			operation_dict["operation"] = "get"
			operation_dict["key"]=key
		operations.append(operation_dict)
	return operations
	
print(readFromConfig())