from datetime import datetime

def breakdownSize(space):
	"""
	Create a human readable break down of the provided size.
	Will go up to petabytes.
	
	@param space: Size in Bytes 
	"""
	if space > 0:
		bytes = space % 1024
		space = int(space/1024)
		kbytes = space % 1024
		space = int(space/1024)
		mbytes = space % 1024
		space = int(space/1024)
		gbytes = space % 1024
		space = int(space/1024)
		tbytes = space % 1024
		space = int(space/1024)
		pbytes = space % 1024
		return {'b': bytes, 'k': kbytes, 'm': mbytes, 'g': gbytes, 't': tbytes, 'p': pbytes}
	else:
		return {'b': 0, 'k': 0, 'm': 0, 'g': 0, 't': 0, 'p': 0}
	
def formatSize(space, length = 6):
	"""
	Provide a human readable fance presentation of the provided bytes. 
	
	@param space: Size in Bytes
	@param length: How far back to go from 1st breakdown. EX: 1=1PB 2=1PB 1TB 3=1PB 1TB 1GB
	"""
	total = breakdownSize(space)
	tStr = ''
	currentLength = 0
	if total['p'] != 0:
		tStr += str(total['p']) +'PB '
		currentLength +=1
	if total['t'] != 0 and length >= currentLength:
		tStr += str(total['t']) +'TB '
		currentLength +=1
	if total['g'] != 0 and length >= currentLength:
		tStr += str(total['g']) +'GB '
		currentLength +=1
	if total['m'] != 0 and length >= currentLength:
		tStr += str(total['m']) +'MB '
		currentLength +=1
	if total['k'] != 0 and length >= currentLength:
		tStr += str(total['k']) +'KB '
		currentLength +=1
	if total['b'] != 0 and length >= currentLength:
		tStr += str(total['b']) +'B '
		currentLength +=1
		
	if tStr == '':
		tStr = '0B'
		
	return tStr

class MemcachedClusterStats(object):
	def __init__(self, mcClient):
		"""
		Provides a OO based approch at reading the stats from a givin Memcached Client instance.
		
		@param mcClient: Memcached Client Instance 
		"""
		self.servers = []
		for server in mcClient.get_stats():
			self.servers.append(MemcachedServerStats(server[0], server[1]))
	
	def getServers(self):
		"""
		Return the list of MemcachedServerStats
		"""
		return self.servers
	
	def getTotalItems(self):
		"""
		Returns the total count of items ever in the cluster
		"""
		return self._getServersAttrib('TotalItems')
	
	def getItems(self):
		"""
		Returns the total count of items currently in the cluster
		"""
		return self._getServersAttrib('CurrItems')
	
	def getTotalConnections(self):
		"""
		Returns the total number of connections ever to the cluster
		"""
		return self._getServersAttrib('TotalConnections')
	
	def getConnections(self):
		"""
		Returns the total number of current active connections
		"""
		return self._getServersAttrib('CurrConnections')
	
	def getHits(self):
		"""
		Returns the total number of Get Requests that succeeded 
		"""
		return self._getServersAttrib('GetHits')
	
	def getMisses(self):
		"""
		Returns the total number of Get Requests that failed 
		"""
		return self._getServersAttrib('GetMisses')
	
	def getGets(self):
		"""
		Returns the total number of get requests preformed
		"""
		return self._getServersAttrib('CMDGet')
	
	def getSets(self):
		"""
		Returns the total number of set requests preformed
		"""
		return self._getServersAttrib('CMDSet')
	
	def getEvictions(self):
		"""
		Returns the total number of evictions
		"""
		return self._getServersAttrib('Evictions')
	
	def getTotalSpace(self):
		"""
		Returns the total size of the cluster
		"""
		return self._getServersAttrib('LimitMaxBytes')
	def getFormatedTotalSpace(self):
		"""
		Returns the total size of the cluster in a pretty formated string
		"""
		return formatSize(self.getTotalSpace())
	
	def getFreeSpace(self):
		"""
		Returns the current free space of the cluster
		"""
		return self._callServersFunc('getFreeSpace')
	def getFormatedFreeSpace(self):
		"""
		Returns the current free space of the cluster in a pretty formated string
		"""
		return formatSize(self.getFreeSpace())
	
	def getUsedSpace(self):
		"""
		Returns the current used space of the cluster
		"""
		return self._getServersAttrib('Bytes')
	def getFormatedUsedSpace(self):
		"""
		Returns the current used space of the cluster in a pretty formated string
		"""
		return formatSize(self.getUsedSpace())
	
	def getRequestRate(self):
		"""
		Returns the Request rate of the overall cluster
		"""
		return self._callServersFunc('getRequestRate')
	
	def getHitRate(self):
		"""
		Returns the Hit rate of the overall cluster
		"""
		return self._callServersFunc('getHitRate')
	
	def getMissRate(self):
		"""
		Returns the Miss rate of the overall cluster
		"""
		return self._callServersFunc('getMissRate')
	
	def getSetRate(self):
		"""
		Returns the Set rate of the overall cluster
		"""
		return self._callServersFunc('getSetRate')
	
	def getGetRate(self):
		"""
		Returns the Get rate of the overall cluster
		"""
		return self._callServersFunc('getGetRate')
	
	def getEvictionRate(self):
		"""
		Returns the Eviction rate of the overall cluster
		"""
		return self._callServersFunc('getEvictionRate')
	
	def getRequestRateAvg(self):
		"""
		Returns the Avg Request rate of the overall cluster
		"""
		rate = self._callServersFunc('getRequestRate')
		for server in self.servers:
			rate += server.getRequestRate()
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getSetRateAvg(self):
		"""
		Returns the Avg Set rate of the overall cluster
		"""
		rate = self._callServersFunc('getSetRate')
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getGetRateAvg(self):
		"""
		Returns the Avg Get rate of the overall cluster
		"""
		rate = self._callServersFunc('getGetRate')
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getHitRateAvg(self):
		"""
		Returns the Avg Hit rate of the overall cluster
		"""
		rate = self._callServersFunc('getHitRate')
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getMissRateAvg(self):
		"""
		Returns the Avg Miss rate of the overall cluster
		"""
		rate = self._callServersFunc('getMissRate')
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getEvictionRateAvg(self):
		"""
		Returns the Avg Eviction rate of the overall cluster
		"""
		rate = self._callServersFunc('getEvictionRate')
		if rate > 0:
			return rate/len(self.servers)
		else:
			return 0
	
	def getThreads(self):
		"""
		Returns the total number of active threads in the cluster
		"""
		return self._getServersAttrib('Threads')
	
	def _getServersAttrib(self, attribute):
		"""
		Loops through the current server list and adding up the givin attributes
		
		@param attribute: Attribute to access from each MemcachedServerStats instance
		"""
		total = 0
		for server in self.servers:
			total += server.__getattribute__(attribute)
		return total
	
	def _callServersFunc(self, function):
		"""
		Loops through the current server list and adding up the givin return from the provided function
		
		@param function: Function to call for each MemcachedServerStats instance
		"""
		total = 0
		for server in self.servers:
			total += server.__getattribute__(function)()
		return total
		
class MemcachedServerStats(object):
	def __init__(self, name, items):
		"""
		Represents stats for a single server
		
		@param name: Name of the givin server
		@param items: A dict collection of stats as provided from memcached.Client.get_stats()  
		"""
		#Current Time to base all start up times on
		self.CurrentTime = datetime.today()
		
		#Given name of the server
		self.Name = name
		#Process ID for the memcached instance
		self.PID = items.get('pid', 0)
		#Datetime representation of the uptime
		self.Uptime = datetime.fromtimestamp(int(items.get('uptime', 0)))
		#Unixtimestamp representation of the uptime
		self.UptimeTimestamp = int(items.get('uptime', 0))
		#Datetime representation of the current server times
		self.Time = datetime.fromtimestamp(int(items.get('time', 0)))
		#Unixtimestamp representation of the current server times
		self.Timestamp = int(items.get('time', 0))
		#Version string of the memcached instance
		self.Version = items.get('version', 'N/A')
		#Default size of pointers on the host OS (generally 32 or 64)
		self.PointerSize = int(items.get('pointer_size', 0))
		#Accumulated user time for this process (seconds:microseconds)
		self.RUsageUser = items.get('rusage_user', 0)
		#Accumulated system time for this process (seconds:microseconds)
		self.RUsageSystem = items.get('rusage_system', 0)
		#Current number of active connections
		self.CurrConnections = int(items.get('curr_connections', 0))
		#Total number of connections
		self.TotalConnections = int(items.get('total_connections', 0))
		#Number of connection structures allocated by the serve
		self.ConnectionStructures = int(items.get('connection_structures', 0))
		#Number of Get Requests
		self.CMDGet = int(items.get('cmd_get', 0))
		#Number of Set Requests
		self.CMDSet = int(items.get('cmd_set', 0))
		#Number of Flush Requests
		self.CMDFlush = int(items.get('cmd_flush', 0))
		#Number of Get Hits
		self.GetHits = int(items.get('get_hits', 0))
		#Number of Get Misses
		self.GetMisses = int(items.get('get_misses', 0))
		#Number of Delete Misses
		self.DeleteMisses = int(items.get('delete_misses', 0))
		#Number of Delete Hits
		self.DeleteHits = int(items.get('delete_hits', 0))
		#Number of Incr Misses
		self.IncrMisses = int(items.get('incr_misses', 0))
		#Number of Incr Hits
		self.IncrHits = int(items.get('incr_hits', 0))
		#Number of Decr Misses
		self.DecrMisses = int(items.get('decr_misses', 0))
		#Number of Decr Hits
		self.DecrHits = int(items.get('decr_hits', 0))
		#Number of CAS Misses
		self.CasMisses = int(items.get('cas_misses', 0))
		#Number of CAS Hits
		self.CasHits = int(items.get('cas_hits', 0))
		#Number of CAS Badvals
		self.CasBadval = int(items.get('cas_badval', 0))
		#Total number of bytes read by this server from network
		self.BytesRead = int(items.get('bytes_read', 0))
		#Total number of bytes sent by this server from network
		self.BytesWritten = int(items.get('bytes_written', 0))
		#Number of bytes this server is allowed to use for storage.
		self.LimitMaxBytes = int(items.get('limit_maxbytes', 0))
		#Number of connections currently being accepted
		self.AcceptingConns = int(items.get('accepting_conns', 0))
		#TODO: Find what listen_disabled_num mean
		self.ListenDisabledNum = int(items.get('listen_disabled_num', 0))
		#Number of threads on server
		self.Threads = int(items.get('threads', 0))
		#TODO: Find what conn_yields mean
		self.ConnYields = int(items.get('conn_yields', 0))
		#Current number of bytes used by this server to store items
		self.Bytes = int(items.get('bytes', 0))
		#Number of Items currently in cache
		self.CurrItems = int(items.get('curr_items', 0))
		#Number of Items ever in cache
		self.TotalItems = int(items.get('total_items', 0))
		#Number of evictions on server
		self.Evictions = int(items.get('evictions', 0))
		
	def getFreeSpace(self):
		"""
		Free space of Memcached Instance in Bytes
		"""
		return self.LimitMaxBytes-self.Bytes
	def getFormatedFreeSpace(self):
		"""
		Formated Free space of Memcached Instance
		"""
		return formatSize(self.getFreeSpace())
	def getFormatedUsedSpace(self):
		"""
		Formated Used space of Memcached Instance
		"""
		return formatSize(self.Bytes)
	def getFormatedTotalSpace(self):
		"""
		Formated Total space of Memcached Instance
		"""
		return formatSize(self.LimitMaxBytes)
	def getFormatedBytesRead(self):
		"""
		Formated Net In
		"""
		return formatSize(self.BytesRead)
	def getFormatedBytesWrite(self):
		"""
		Formated Net Out
		"""
		return formatSize(self.BytesWritten)
	
	def getTotalRequests(self):
		"""
		Total number of Request preformed by Memcached Instance
		"""
		return self.CMDSet + self.CMDGet + self.CMDFlush
	
	def getRequestRate(self):
		"""
		Request Rate of Memcached Instance
		"""
		return (float(self.getTotalRequests()))/float(self.UptimeTimestamp)
	
	def getSetRate(self):
		"""
		Set Rate of Memcached Instance
		"""
		return float(self.CMDSet)/float(self.UptimeTimestamp)
	def getGetRate(self):
		"""
		Get Rate of Memcached Instance
		"""
		return float(self.CMDGet)/float(self.UptimeTimestamp)
	def getFlushRate(self):
		"""
		Flush Rate of Memcached Instance
		"""
		return float(self.CMDFlush)/float(self.UptimeTimestamp)
	def getHitRate(self):
		"""
		Hit Rate of Memcached Instance
		"""
		return float(self.GetHits)/float(self.UptimeTimestamp)
	def getMissRate(self):
		"""
		Miss Rate of Memcached Instance
		"""
		return float(self.GetMisses)/float(self.UptimeTimestamp)
	
	def getHitPerc(self):
		return (float(self.GetHits)/(self.GetMisses+self.GetHits))
	
	def getMissPerc(self):
		return (float(self.GetMisses)/(self.GetMisses+self.GetHits))
	
	def getEvictionRate(self):
		"""
		Eviction Rate of Memcached Instance
		"""
		return float(self.Evictions)/float(self.UptimeTimestamp)