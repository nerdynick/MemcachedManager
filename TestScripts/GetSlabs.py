import memcache

mc = memcache.Client(['127.0.0.1:11211','127.0.0.1:11212'], debug=0)
data = []
for s in mc.servers:
    if not s.connect(): continue
    name = '%s:%s (%s)' % ( s.ip, s.port, s.weight )
    serverData = {}
    data.append(( name, serverData ))
    s.send_cmd('stats items')
    readline = s.readline
    while 1:
        line = readline()
        if not line or line.strip() == 'END': break
        item = line.split(' ', 2)
        #0 = STAT
        #1 = ITEM
        #2 = Value
        slab = item[1].split(':', 2)
        #0 = items
        #1 = Slab #
        #2 = Name
        if not serverData.has_key(slab[1]):
            serverData[slab[1]] = {}
            
        serverData[slab[1]][slab[2]] = item[2]
            
        
        
print data