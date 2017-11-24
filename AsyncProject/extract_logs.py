from subprocess import call
import sys
config_file_name = "config.txt"

def get_config_info(config_file_name):
    config = {}
    with open(config_file_name, 'r') as f:
        for line in f:
            if line[0] != '#':
                (key, sep, val) = line.partition('=')
                # if the line does not contain '=', it is invalid and hence ignored
                if len(sep) != 0:
                    val = val.strip()
                    config[key.strip()] = int(
                        val) if str.isdecimal(val) else val
    return config

config = get_config_info(config_file_name)
num_client = config.get('num_client')



for num in range(0,num_client):
	search_string = "Client "+str(num)+" -*"
	output_file = "client"+str(num)+".log"
	command = "grep -ir -hn '"+search_string+"' --include='*_client.log' . > "+output_file
	#print(client_string)
	print(command)
	#grep -ir -hn "Client" --include="*_client.log" . >  client1.log
	#grep -ir -hn "Client" --include="./*_client.log" . >  client1.log
	call(command, shell=True)
