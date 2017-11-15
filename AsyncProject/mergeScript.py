from subprocess import call
import sys
#open('BCR.da', 'w').close()
#subprocess.check_output(['ls','-l']) #all that is technically needed...

param = None
if(len(sys.argv) > 1):
	param = sys.argv[1]

if param is not None and (param == "r" or param == "rm"):
	call('rm ./*.log', shell=True)
elif param == "run":
	call('/Users/sai/packages/pyDistAlgo-1.0.10/bin/dar --message-buffer-size 10000 ./BCR.da', shell=True)
elif param == "merge" or param =="m":
	filenames = ['ByzantineReplica.da','ByzantineHelper.da', 'ByzantineOlympus.da', 'ByzantineClient.da','ByzantineParentProcess.da']
	with open('BCR.da', 'w') as outfile:
	    for fname in filenames:
	        with open(fname) as infile:
	            outfile.write(infile.read())
elif param == None:
	call('rm ./*.log', shell=True)

	filenames = ['ByzantineReplica.da','ByzantineHelper.da', 'ByzantineOlympus.da', 'ByzantineClient.da','ByzantineParentProcess.da']
	with open('BCR.da', 'w') as outfile:
	    for fname in filenames:
	        with open(fname) as infile:
	            outfile.write(infile.read())

	
	call('/Users/sai/packages/pyDistAlgo-1.0.10/bin/dar --message-buffer-size 10000 ./BCR.da', shell=True)
	#call(["/Users/sai/packages/pyDistAlgo-1.0.10/bin/dar"," --message-buffer-size 5000 " ,"./BCR.da"], shell=True)
