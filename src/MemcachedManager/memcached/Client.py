'''
Created on Nov 1, 2010

@author: nick
'''
import memcache
import socket

class MemcachedClient(memcache.Client):
    def get_all(self, keys, key_prefix='', unpickel=True, compressed=False):
        if compressed:
            flag = memcache.Client._FLAG_COMPRESSED
        else:
            flag = 0
            
        values = {}
        for key in keys:
            server, key = self._get_server(key)
            
            self._statlog('get_all')
    
            for server in self.servers:
                try:
                    server.send_cmd("%s %s" % ('get', key))
                    rkey = flags = rlen = None
                    rkey, flags, rlen = self._expectvalue(server)
                    if not rkey:
                        value = None
                    else:
                        value = self._recv_value(server, flag, rlen, unpickel=unpickel)
                        server.expect("END")
                except (memcache._Error, socket.error), msg:
                    if isinstance(msg, tuple):
                        msg = msg[1]
                    server.mark_dead(msg)
                    
                server = str(server)
                if not values.has_key(server):
                    values[server] = {}
                    
                values[server][key] = value
                
        return values