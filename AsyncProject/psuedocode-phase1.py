


				Psuedo Code for Byzantine Chain Replication:


Sri Krishna Jayadev Peddhibotla(111499827)
Sai Madan Mohan Reddy Patlolla(111499340)
												


#Global variable to Hold all the statements
Statements = {}

class OrderStatement():
	slot = None
	operation = None
	signature = None
	def __init__(self,slot,operation,signature):
		self.slot = slot
		self.operation = operation
		self.signature = signature

class ResultProof():
	operation = None
	Replica_Id = None
	Config_Id =None
	Result_Hash = []

	def __init__(self,operation,Replica_Id,Config_Id):
		self.operation = operation
		self.Replica_Id = Replica_Id
		self.Config_Id = Config_Id

	def add_result_hash(result):
		#get asyymetric key pair from olympus by passing replica_id
		public_key,privatekey = get_assymentric_key_pair(Replica_Id)
		result_hash_value = compute_hash(result)
		Result_Hash.append(result_hash_value)


class OrderProof():
	slot = None
	operation = None
	Replica_Id = None
	Config_Id =None
	OrderStatements = []

	def __init__(self,slot,operation,Replica_Id,Config_Id):
		self.slot = slot
		self.operation = operation
		self.Replica_Id = Replica_Id
		self.Config_Id = Config_Id

	def add_order_statment(Replica_Id):
		#get asyymetric key pair from olympus by passing replica_id
		public_key,privatekey = get_assymentric_key_pair(Replica_Id)
		signature = compute_digital_signature(privatekey)
		new_order_statement = OrderStatement(slot,operation,signature)
		OrderStatements.append(new_order_statement)
		

class RequestCache():
	result = None
	result_proof = None
	def __init__(self,result,result_proof):
		self.result = result 
		self.result_proof = result_proof

class Replica():
	Replica_Id = None
	mode = None
	Data = None
	#result cache will hold the result and result-proof for request_id
	#cached at the replica
	result_cache = {}

	#replica's history will hold the set of order-proofs
	history = None
	def __init__(self,Replica_Id)
		self.mode = "ACTIVE"
		self.Replica_Id = Replica_Id

	def perform_operation(operation):
		#perform the operation on the data and return the computed result
		return result

class Shuttle():
	order_proof = None
	result_proof = None
	def __init__(self,slot,operation,Replica_Id,Config_Id):
		self.order_proof = OrderProof(slot,operation,Replica_Id,Config_Id)
		self.result_proof = ResultProof(operation,Replica_Id,Config_Id)

	def add_to_order_proof(replica_id):
		order_proof.add_order_statment(replica_id)
	def add_to_result_proof(result):
		result_proof.add_result_hash(result)

class CheckPointShuttle():
	running_state = {}
	def add_hash_of_running_state(replica_id,history):
		self.running_state[replica_id] = compute_hash(history)
	def get_hash_for_replica(replica_id):
		#returns the hash of running state for a replica
		return running_state[replica_id]

class olympus():

	Replica_Chain = {}
	Replica_Asymmetric_keys = []
	count_of_replicas = None
	timer = None
	check_pointing_milestone = None
	Tolerance_Level = None 

	def reset_all_data():
		#remove all the previous config details
		Replica_Chain = {}
		Replica_Asymmetric_keys = []
		count_of_replicas = None
		timer = None
		check_pointing_milestone = None
		Tolerance_Level = None 

	def initialize_replica_with_history(longest_history,data):
		for Replica_Id in range(count_of_replicas):
			Replica_Chain[Replica_Id].history=longest_history
			Replica_Chain[Replica_Id].data = data

	def Configuration(longest_history,data):

		#perform reconfiguration
		if(longest_history is not None):
			reset_all_data()

		#geberate configuration and obtain config-id
		Config_Id = get_random_guid()

		#setup the replicas and start them
		initialize_setup()
		setup_replicas()

		if(longest_history is not None):
			initialize_replica_with_history(longest_history,data)

	def get_assymentric_key_pair(replica_id):
		keypair = Replica_Asymmetric_keys[Replica_Id]
		(private_key,public_key) = (keypair["public_key"],keypair["private_key"])
		return (private_key,public_key)

	#create a privatekey,public key pair for a replica 
	def generate_assymentric_key_pair():
		pass

	#creating a set of 2T+1 replicas with empty history and generate
	#assymetric key pair for each replica
	def setup_replicas():
		Replica_Chain = [Replica(i) for i in range(count_of_replicas)]
		for i in range(count_of_replicas):
			(public_key,private_key) = generate_assymentric_key_pair()
			Replica_Asymmetric_keys.append({"public_key":public_key,"private_key":private_key})
			#`Set all replica parameters

			
	def initialize_setup():
		#get the Tolerance Value and create 2T+1 replicas
		Tolerance_Level = readFromConfig()
		timer_expiry_limit =readFromConfig()
		check_pointing_milestone = readFromConfig()
		count_of_replicas = 2*Tolerance_Level + 1
		setup_replicas(count_of_replicas)

	def start_processes():
		#start 2T+1 replica processes
		for i in range(count_of_replicas):
			#start the replica process to process  the client requests
			start_replica(i)

	def get_active_configuration_from_olympus():
		#send the active configuration id

	def get_replica_information_from_olympus():
		#send the replica list to the client

	def get_head_tail_for_current_config(Config_Id):
		#return the head_replica,tail_replica

	def get_latest_configuration():
		#return the latest available configuration

	def get_current_slot_number():
		#checks the head_replica_used_slots and
		#return the next available slot

	def start_timer_at_head_replica():
		#start the timer at replica in the case of
		#the retransmitted request from the client
		start_timer(timer)

	def is_timer_expired():
		if timer >= timer_expiry_limit:
			return true
		else:
			return false




	def issue_wedge_statements():
		#find the maximal order proofs
		max_size = Replica_Chain[head_replica].history.size()
		distinct_replicas = false
		current_quorum_size = 1 
		cryptographic_hash_of_head = compute_hash(head_replica)
		longest_history = Replica_Chain[head_replica].history
		data = head.data
		for current_replica in Replica_Chain.keys:
			replica_history = Replica_Chain[current_replica].history
			current_replica_history_size = replica_history.size()
			if(current_replica_history_size != max_size):
				#get the  difference history of order proofs
				diff_history = Replica_Chain[head_replica].history[current_replica_history_size:]

				for orderproof in diff_history:
					slot = get_current_slot_number(current_replica)
					operation = orderproof.operation
					#assign the operation to the slot number and create an 
					#order proof 
					orderproof = OrderProof(slot,operation,current_replica,Config_Id)
					#adds order statement digitally signed by head_replica
					orderproof.add_order_statment(current_replica)

					#perform the operation and get the result
					result = current_replica.perform_operation(operation)

					Replica_Chain[current_replica].history.append(orderproof)

					replica_history = Replica_Chain[current_replica].history
	
				cryptographic_hash_of_current_replica = compute_hash(replica_history)
				if match(cryptographic_hash_of_head,cryptographic_hash_of_current_replica) is True
					current_quorum_size = current_quorum_size + 1
		
			if quorum_size == Tolerance_Level+1:
			   configuration(longest_history,data)

	#Upon successful vaildation of the check pointproof truncate history at each replica
	def truncate_histories(prev_replica,check_point_proof):
		
		#truncaate the history of the replica to till the previous milestone
		Replica_Chain[prev_replica].history[0:check_pointing_milestone].remove()
		prev_replica = get_prev_replica(prev_replica)
		if prev_replica != head_replica:
			cache_result_for_request(prev_replica,check_point_proof)


	def check_pointing(replica_Id,check_point_shuttle):
		#perform check pointing which is inititated by head after
		#every miletstone perform truncation of history at each replica
		if replica_Id == head_replica:
			#create the check pointg
			check_point_shuttle = CheckPointShuttle()
			#get the history i.e, the current running state of the replica
			#so as to calculate hash of the running state
			history_replica = Replica_Chain[head_replica].history
			check_point_shuttle.add_hash_of_running_state(history_replica)
		else:

			#get the history i.e, the current running state of the replica
			#so as to calculate hash of the running state
			history_replica = Replica_Chain[replica_Id].history
			check_point_shuttle.add_hash_of_running_state(history_replica)

			if replica_Id == tail_replica:
				#get the running state hash of all replicas
				running_state_total = CheckPointShuttle.running_state()
				#perform validation so that all runnign states match
				for i in range(0,running_state_total.length()-1)
					if(running_state_total[i] != running_state_total[i+1])
						#running states are not commong error
						return error:
				truncate_histories(Replica_Id,CheckPointShuttle)
			else:
				#forward the checkpointing shuttle to next replica  
				next_replica = get_next_replica(replica_Id)
				check_pointing(next_replica,check_point_shuttle):


	def send_request_to_replica(request_id,operation,replica_id,slot_number = 0,shuttle=None,retransmit=false):
		#immutable state is when the replica has already gave wedged statements or is in a invalid statements
		if replica == immutable_state:
			return error

		if replica_Id == head_replica:
			if(head_replica.result_cache[request_id] is not None):
				result_cache_obj = result_cache[request_id]
				result = result_cache_obj.result
				result_proof = result_cache_obj.result_proof
				return (result,result_proof)
			else:
				if retransmit is True:
					start_timer_at_head_replica()
					#abort all the processeses
					return

				#request a new operation
				slot_number = get_current_slot_number()


				#create a shuttle for the orderproof and resultproof propagation
				shuttle = Shuttle(slot_number,operation,head_replica,Config_Id)

				#assign the operation to the slot number and create an 
				#order proof 
				orderproof = OrderProof(slot,operation,head_replica,Config_Id)
				#adds order statement digitally signed by head_replica
				orderproof.add_order_statment(head_replica)

				#perform the operation and get the result
				result = head_replica.perform_operation(operation)

				Replica_Chain[head_replica].history.append(orderproof)


				#add the orderproof and the resultproof the shuttle
				shuttle.add_to_order_proof(replica_id)
				#it will add the hashed result
				shuttle.add_to_result_proof(result)

				# add to global statement signed by replica
				statements.add(orderproof)

				#this returns true only in the case when the timer is started
				#otherwise it returns false
				if(head_replica.is_timer_expired()):
					issue_wedge_statements()
					return

				#send the shuttle,slot operation and the result to the next replica
				send_request_to_replica(request_id,operation,replica_Id,slot_number,shuttle)


				if slot_number % check_pointing_milestone == 0:
					check_pointing()

		else:
				#during the retransmission if the client has the cached result it will 
				#return the result and the result_proof the the client
				if(Replica_Id.result_cache[request_id] is not None):
					result_cache_obj = result_cache[request_id]
					result = result_cache_obj.result
					result_proof = result_cache_obj.result_proof
					return (result,result_proof)
				elif retransmit is True:
					#replica doesnot recognize the operation as it is directly sent by client it sends the request
					#to head
					send_request_to_replica(request_id,operation,head_replica,retransmit=true)
					return
			
				#this returns true only in the case when the timer is started
				#otherwise it returns false
				if(head_replica.is_timer_expired()):
					#abort all the processeses
					return

				#use the shuttle sent by previous replica and slot number

				#assign the operation to the slot number and create an 
				#order proof 
				orderproof = OrderProof(slot_number,operation,Replica_Id,Config_Id)
				#adds order statement digitally signed by head_replica
				orderproof.add_order_statment(replica_id)

				#perform the operation and get the result
				result = replica_id.perform_operation(operation)

				Replica_Chain[replica_id].history.append(orderproof)


				#add the orderproof and the resultproof the shuttle
				shuttle.add_to_order_proof(replica_id)
				#it will add the hashed result
				shuttle.add_to_result_proof(result)

				# add to global statement signed by replica
				statements.add(orderproof)

				if replica_Id == tail_replica:
					#send result and result proof to the client
					curr_result_cache_obj = {}
					curr_result_cache_obj.result = result_cache_obj.result
					curr_result_cache_obj.result_proof = result_cache_obj.result_proof
					tail_replica.result_cache[request_id] = curr_result_cache_obj
					prev_replica = get_prev_replica(tail_replica)
					cache_result_for_request(request_id,result,result_proof,prev_replica)
				else:
					#forward the shuttle to next replica and 
					next_replica = get_next_replica(replica_Id)
					send_request_to_replica(request_id,operation,next_replica,slot_number,shuttle,head=true)

	def cache_result_for_request(request_id,result,result_proof,prev_replica):
		curr_result_cache_obj = {}
		curr_result_cache_obj.result = result_cache_obj.result
		curr_result_cache_obj.result_proof = result_cache_obj.result_proof
		prev_replica.result_cache[request_id] = curr_result_cache_obj
		prev_replica = get_prev_replica(prev_replica)
		if prev_replica != head_replica:
			cache_result_for_request(request_id,result,result_proof,prev_replica)

	def request_response_from_replica(request_id,tail_replica):
		if result_cache_obj[request_id] is not None:
				result_cache_obj = result_cache[request_id]
				result = result_cache_obj.result
				result_proof = result_cache_obj.result_proof
				return (result,result_proof)
		else:
			return None


class Client():
	#
	timer_expiry_limit = None
	request_id = None
	list_of_replicas_for_current_config = None
	def start_client_timer():
		#using lamport logical clock start the client timer 
		#before sending a request.
		
	def is_timer_expired():
		# send timer expired status when timer is
		#expired

	def get_active_configuration():
		#get the current active configuration id of replicas
		#from the olympus
		get_active_configuration_from_olympus()

	def get_random_guid():
		#generates  a random guid 

	def start_client():
		#starting the client process 

		#get the current active configuration from the olympus
		Config_Id = get_active_configuration()

		#get the replica processes information from the current
		#configuration
		list_of_replicas_for_current_config = get_replica_information_from_olympus(Config_Id)

		head_replica,tail_replica = get_head_tail_for_current_config(Config_Id)
		#read the client timer expiry
		#from the provided configuration file

		timer_expiry_limit = readFromConfig()

		#read operation from config
		
		while (operation = readFromConfig()) is not None:
			
			start_client_timer();
			request_id = get_random_guid()
			#initial transmission send the request to head_replica
			send_request_to_replica(request_id,operation,head_replica)

			while !is_timer_expired() and (response = request_response_from_replica(request_id,tail_replica) is not None):					
				result = response[0]
				result_proof = response[1]
				if is_valid_response(result,result_proof) is True:
					#show the result of the requested operation
				else:
					#request for reconfiguration
			else:

				#here the timer is expired and the client retransmits its
				#request to all the replicas in the current configuration
				for replica_id in list_of_replicas_for_current_config:
					send_request_to_replica(request_id,operation,replica_id)
					response = request_response_from_replica(request_id,replica_id)
					#if the replica is immutable it responds to the client
					#with an error statement
					if response is Error:
						start_client_timer();
						#get the Latest configuration from the olympus
						Config_Id = get_latest_configuration()

						#get the replica processes information from the current
						#configuration
						list_of_replicas_for_current_config = get_replica_information_from_olympus(Config_Id)

						head_replica,tail_replica = get_head_tail_for_current_config(Config_Id)

						# transmission to head replica of new configuration,send the request to head_replica
						send_request_to_replica(request_id,operation,head_replica)
						while !is_timer_expired() and (response = request_response_from_replica(request_id,tail_replica) is not None):
							result = response[0]
							result_proof = response[1]
							if is_valid_response(result,result_proof) is True:
								#show the result of the requested operation
							else:
								#request for reconfiguration 
					else:
						#if a correct replica that receives the request has the result
						#shuttle cached it returns the result along with the result proof
						result = response[0]
						result_proof = response[1]
						if is_valid_response(result,result_proof) is True:
							#show the result of the requested operation
						else:
							#request for reconfiguration 



