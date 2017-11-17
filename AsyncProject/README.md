# Implementation of Byzantine Chain Replication - Phase 2

# PLATFORM
Dist Algo Version = pyDistAlgo 1.0.9
Python Version= Python 3.6.2 Anaconda, Inc.
Operating System: Windows, Linux(in VM), OSX
Types of Hosts: 2 OSX hosts


# INSTRUCTIONS
Install pyDistAlgo before running the mergescript
>pip install pyDistAlgo

Edit the following fields of the mergescript.py before executing it:
	host_ip = "<enter source  ip>"
	dest_ip = "<enter destination ip>"
	NodeName = "<set-value as 'parent' in the source system>"

Log files are generated post execution as follows:
> timestamp_ParentProcess.log
> timestamp_Replica.log
> timestamp_Olympus.log
> timestamp_Client.log
> timestamp_MainModule.log


# WORKLOAD GENERATION

For pseudorandom client workload generation, we, used a pre-defined list of operations and selecting requested number of operrations randomly from these fixed set of operations.


# BUGS and LIMITATIONS
Forward request failures not thoroughly tested
Supports only for T=1; for T=2 we are observing a "message too big exception" that needs to be looked into.


# CONTRIBUTIONS
Sai Madan Mohan Reddy Patlolla: Replica, Olympus, Critical debugging and fixing issues while development
Sri Krishna Jayadev Peddibhotla: Client, ParentProcess, Logging, Digital Signature Mechanisms


# MAIN FILES
ByzantineClient.da
ByzantineHelper.da
ByzantineOlympus.da
ByzantineReplica.da
ByzantineParentProcess.da
mergescript.py


# CODE SIZE
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
DAL                              1            171              4           1095

# LANGUAGE FEATURE USAGE
await()
receive()
received()
send()
process
timeout()
config() - various params
lists
dicts


# OTHER COMMENTS
Due to submission time constraints we could only do a breif readme, excuse us if we had missed out on some detailed explaination where expected. 