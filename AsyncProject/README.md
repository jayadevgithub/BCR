# Implementation of Byzantine Chain Replication - Phase 3

# PLATFORM
Dist Algo Version = pyDistAlgo 1.0.
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
For pseudorandom client workload generation, we used a pre-defined list of operations and are selecting the requested number of operations randomly from these fixed set of operations.


# BUGS and LIMITATIONS
Intermittent issues with checkpotinting when multiple clients are served


# CONTRIBUTIONS
Sai Madan Mohan Reddy Patlolla: 
>Handling functionalities of Replica, Olympus, checkpointing, catch up, failure triggers and failures

Sri Krishna Jayadev Peddibhotla:
>Handling functionalities of Client, ParentProcess, Digital Signature, Reconfiguration, testing and debugging. 


# MAIN FILES
ByzantineClient.da
ByzantineHelper.da
ByzantineOlympus.da
ByzantineReplica.da
ByzantineParentProcess.da
mergescript.py


# CODE SIZE
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
DAL                              1            603              4           2589
-------------------------------------------------------------------------------


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
nacl.signing.*
logger


# OTHER COMMENTS
NA