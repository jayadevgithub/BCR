from subprocess import call
import sys
#open('BCR.da', 'w').close()
#subprocess.check_output(['ls','-l']) #all that is technically needed...
distalgo_compiler_path = "/Users/sai/Downloads/pyDistAlgo-1.0.11/bin/dar"

#config_file_name = "failure_catchup_message.txt"

#config_file_name = "failure_change_operation.txt"

#config_file_name =  "failure_checkpointing.txt"

#config_file_name = "failure_crash.txt"

#config_file_name = "failure_drop_result_statement_at_tail_replica.txt"

#config_file_name = "failure_drop_undetected.txt"

#config_file_name = "failure_extraop.txt"

#config_file_name = "failure_forwarded_request.txt"

#config_file_name = "failure_increment_slot.txt"

#config_file_name = "failure_invalid_order_signature.txt"

#config_file_name = "failure_invalid_result_signature.txt"

#config_file_name = "failure_multiple_configurations.txt"

#config_file_name = "failure_shuttle_drop.txt"

#config_file_name = "testcase_checkpointing.txt"

#config_file_name = "testcase_perform900.txt"

#config_file_name = "testcase_head_change_op.txt"

config_file_name = "testcase_tail_double_fail.txt"



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



param = None
if(len(sys.argv) > 1):
	param = sys.argv[1]

if param is not None and (param == "r" or param == "rm"):
	call('rm ./*.log', shell=True)
elif param == "run":
	call(distalgo_compiler_path+' --message-buffer-size 10000 ./BCR.da', shell=True)
elif param == "merge" or param =="m":
	filenames = ['ByzantineReplica.da','ByzantineHelper.da', 'ByzantineOlympus.da', 'ByzantineClient.da','ByzantineParentProcess.da']
	with open('BCR.da', 'w') as outfile:
	    for fname in filenames:
	        with open(fname) as infile:
	            outfile.write(infile.read())
elif param == "ex":
	num_client = config.get('num_client')
	for num in range(0,num_client):
		search_string = "Client "+str(num)+" -*"
		output_file = "Client"+str(num)+".log"
		command = "grep -ir -hn '"+search_string+"' --include='*_client.log' . > "+output_file
		call(command, shell=True)

	t = config.get('t')

	for num in range(0,2*t+1):
		search_string = "Replica "+str(num)+" -*"
		output_file = "Replica"+str(num)+".log"
		command = "grep -ir -hn '"+search_string+"' --include='*_replica.log' . > "+output_file
		call(command, shell=True)

	client_rename_command = "mv 2017*_client.log 1.Client.log"
	replica_rename_command = "mv 2017*_replica.log 2.Replica.log"
	olympus_rename_command = "mv 2017*_olympus.log 3.Olympus.log"
	mainmodule_rename_command = "mv 2017*_MainModule.log 4.MainModule.log"
	parent_process_rename_command = "mv 2017*_ParentProcess.log 5.ParentProcess.log"	
	call(client_rename_command, shell=True)
	call(replica_rename_command, shell=True)
	call(olympus_rename_command, shell=True)
	call(mainmodule_rename_command, shell=True)
	call(parent_process_rename_command, shell=True)

elif param == None:
	call('rm ./*.log', shell=True)

	filenames = ['ByzantineReplica.da','ByzantineHelper.da', 'ByzantineOlympus.da', 'ByzantineClient.da','ByzantineParentProcess.da']
	with open('BCR.da', 'w') as outfile:
	    for fname in filenames:
	        with open(fname) as infile:
	            outfile.write(infile.read())

	
	call(distalgo_compiler_path+' --message-buffer-size 100000 ./BCR.da', shell=True)
	#call(["/Users/sai/packages/pyDistAlgo-1.0.10/bin/dar"," --message-buffer-size 5000 " ,"./BCR.da"], shell=True)
