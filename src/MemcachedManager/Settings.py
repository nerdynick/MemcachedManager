import os
from Clusters import Cluster
from Servers import Server
import pickle
		
def getSaveLocation():
	try:
		path = os.path.join(os.environ.get('HOME', os.environ.get('HOMEPATH', os.getcwd())), '.MemcachedManager')
		if not os.path.exists(path):
			os.makedirs(path, 0755)
		return path
	except Exception, e:
		return os.getcwd()

class Settings:
	settings = None
	servers = None
	
	def __init__(self):
		if self.settings is None:
			self.settings = GlobalSettings()
		
		if self.servers is None:
			self.servers = ServerSettings()
			
	def save(self):
		self.settings.save()
		self.servers.save()

class GlobalSettings:
	__settings = {}
	
	def __init__(self):
		self.__dict__ = self.__settings
		self.loadConfig()
		
	def loadConfig(self):
		if not self.__dict__.has_key('configPath') or self.configPath is None:
			self.configPath = os.path.join(getSaveLocation(), 'preferences.ini')
			
		if not self.__dict__.has_key('config') or self.config is None:
			if os.path.exists(self.configPath) is not True:
				self.config = {
							'Graphs': {
									'HitMiss': '#CF8442',
									'GetSet': '#CF8442',
									'Pie': [
										('#CF8442','#824C1D'),
										('#CF612D','#823410'),
										('#CF3615','#821D07'),
										('#CF2937','#82000B'),
										('#CFA14A','#825A10'),
										('#CFB248','#82690F'),
										('#CFC442','#82790B'),
										('#C0CF46','#75820E')
										]
									},
							'Stats': {
									'RefreshInterval': 5,
									'AutoRefresh': True
									}
							}
			else:
				self.config = pickle.load(open(self.configPath, 'rb'))
		
	def save(self):			
		pickle.dump(self.config, open(self.configPath, 'wb'))

class ServerSettings:
	__settings = {}
	
	def __init__(self):
		self.__dict__ = self.__settings
		self.loadConfig()
		self.loadClusters()
		
	def __del__(self):
		self.save()
			
	def loadConfig(self):
		if not self.__dict__.has_key('configPath') or self.configPath is None:
			self.configPath = os.path.join(getSaveLocation(), 'servers.ini')
			
		if not self.__dict__.has_key('config') or self.config is None:
			if os.path.exists(self.configPath) is not True:
				self.config = {'clusters': []}
			else:
				self.config = pickle.load(open(self.configPath, 'rb'))
			
	def loadClusters(self):
		if not self.__dict__.has_key('clusters') or self.clusters is None:
			self.clusters = []
			for cluster in self.config['clusters']:
				tCluster = Cluster(cluster['name'])
				for server in cluster['servers']:
					tServer = Server(
									 server['name'],
									 server['ip'],
									 server['port']
									 )
					tCluster.addServer(tServer)
				self.clusters.append(tCluster)
				
			if len(self.clusters) <= 0:
				self.addDefaults()
		
	def addDefaults(self):
		tCluster = Cluster('Default Cluster')
		tServer = Server('Demo Server', '127.0.0.1', '11211')
		tCluster.addServer(tServer)
		self.addCluster(tCluster)
			
	def save(self):
		self.config['clusters'] = []
		for cluster in self.clusters:
			self.config['clusters'].append(cluster.save())
			
		pickle.dump(self.config, open(self.configPath, 'wb'))
		
	def getClusters(self):
		return self.clusters
	
	def getCluster(self, name):
		for cluster in self.clusters:
			if cluster.name == name:
				return cluster
		return None
			
	def getClusterByMenuItem(self, action):
		for cluster in self.clusters:
			if cluster.menuItems['actions']['delete'] == action:
				return cluster
			elif cluster.menuItems['actions']['set'] == action:
				return cluster
		return None
	
	def getServerByMenuItem(self, action):
		for cluster in self.clusters:
			for server in cluster.getServers():
				if server.menuItems['actions']['delete'] == action:
					return server
		return None
	
	def getServers(self, cluster):
		return cluster.getServers()
	
	def getAllServers(self):
		servers = []
		for cluster in self.clusters:
			servers.extend(cluster.getServers())
		return servers
	
	def getLength(self):
		return len(self.clusters)
	
	def addCluster(self, cluster):
		self.clusters.append(cluster)
		self.save()
		
	def deleteCluster(self, cluster):
		index = self.clusters.index(cluster)
		cluster.delete()
		self.clusters.pop(index)
	
	def addServer(self, cluster, name, ip, port):
		server = Server(name, ip, port)
		cluster.addServer(server)
		self.save()
		return server