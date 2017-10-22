import random

def pseudorandom_workload_gen(seed, count):
		random.seed(seed)
		list_operations = ["put('movie','star')",
							"append('movie',' wars')",
							"get('movie')",
							"put('jedi','luke skywalker)",
							"slice('jedi','0:4'); get('jedi')"]

		list_random_operations = []
		
		for i in range(count):
			list_random_operations.append(list_operations[random.randint(0,len(list_operations)-1)])

		return "; ".join(list_random_operations)


def process_operation(operation):
	output('inside process operation')
    if operation["operation"] is "put":
		key = operation["key"]
		value = operation["value"]
		data_object[key] = value
		return "OK"
    elif operation["operation"] is "get":
        key = operation["key"]
        value = data_object[key]
        return value
    elif operation["operation"] is "slice":
        key = operation["key"]
        if key in data_object:
            return "Error"
        index1 = int(operation["value1"])
        index2 = int(operation["value2"])
        value = data_object[key]
        value = value[index1:index2]
        data_object[key] = value
        return value
    elif operation["operation"] is "append":
        key = operation["key"]
        if key in data_object:
            return "Error"
        value = operation["value"]
        value = value + data_object[key]
        return "OK"



def getWorkLoad():
		config = {}
		with open('config.txt','r') as f:
		    for line in f:
		        if line[0] != '#':
		          (key,sep,val) = line.partition('=')
		          # if the line does not contain '=', it is invalid and hence ignored
		          if len(sep) != 0:
		              val = val.strip()
		              config[key.strip()] = int(val) if str.isdecimal(val) else val
		workload =  config.get('workload['+str(2)+']')
		if("pseudorandom" in workload):
			open_brace_index = workload.find("(")
			comma_index = workload.find(",")
			close_brace_index = workload.find(")")

			seed = int(workload[open_brace_index+1:comma_index].strip())
			count = int(workload[comma_index+1:close_brace_index].strip())

			workload = pseudorandom_workload_gen(seed,count)

		workload = workload.split(';')
		operations = []
		for i in range(0,len(workload)):
			item = workload[i].strip()
			print(item)
			#print("put" in item)
			operation_dict = {}
			if "put" in item :
				first_occur = item.find("'")
				#print(first_occur)
				second_occur = item.find("'",first_occur+1)
				#print(second_occur)
				key = item[first_occur+1:second_occur].strip()
				first_occur = item.find("'",second_occur+1)
				second_occur = item.find("'",first_occur+1)
				value = item[first_occur+1:second_occur].strip()
				operation_dict["operation"] = "put"
				operation_dict["key"]=key
				operation_dict["value"]=value
			elif "append" in item:
				first_occur = item.find("'")
				#print(first_occur)
				second_occur = item.find("'",first_occur+1)
				#print(second_occur)
				key = item[first_occur+1:second_occur].strip()
				first_occur = item.find("'",second_occur+1)
				second_occur = item.find("'",first_occur+1)
				value = item[first_occur+1:second_occur].strip()
				operation_dict["operation"] = "append"
				operation_dict["key"]=key
				operation_dict["value"]=value
			elif "slice" in item:
				first_occur = item.find("'")
				#print(first_occur)
				second_occur = item.find("'",first_occur+1)
				#print(second_occur)
				key = item[first_occur+1:second_occur].strip()
				first_occur = item.find("'",second_occur+1)
				second_occur = item.find("'",first_occur+1)
				value = item[first_occur+1:second_occur].strip()
				operation_dict["operation"] = "slice"
				operation_dict["key"]=key
				slice_indices = value.split(":")
				operation_dict["value1"] = slice_indices[0].strip()
				operation_dict["value2"] = slice_indices[1].strip()
				print(key)
				print(operation_dict)
			elif "get" in item:	
				first_occur = item.find("'")
				#print(first_occur)
				second_occur = item.find("'",first_occur+1)
				#print(second_occur)
				key = item[first_occur+1:second_occur].strip()
				operation_dict["operation"] = "get"
				operation_dict["key"]=key
			operations.append(operation_dict)
		return operations



operations = getWorkLoad()
for operation in operations:
	process_operation(operation)