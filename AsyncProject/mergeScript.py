from subprocess import call
#open('BCR.da', 'w').close()
#subprocess.check_output(['ls','-l']) #all that is technically needed...
filenames = ['ByzantineReplica.da', 'ByzantineOlympus.da', 'ByzantineClient.da']
with open('BCR.da', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            outfile.write(infile.read())

call(["/home/jay/Downloads/pyDistAlgo-1.0.9/bin/dar", "./BCR.da"])
#print(subprocess.check_output(['/Users/sai/Courses/Async/pyDistAlgo-1.0.9/bin/dar','./BCR.da']))
