import memcache
import cStringIO
import json

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

value = """
["foo", {"bar":["baz", null, 1.0, 2]}]
"""
for i in range(1,10):
    result = mc.set("TestC_"+ str(i), value)
    print "Set: TestC_"+ str(i) +" - ", result