import memcache

mc = memcache.Client(['127.0.0.1:11211','127.0.0.1:11212'], debug=0)
for i in range(1,100000):
    result = mc.get("Test_Key_"+ str(i))
    print "Set: Test_Key_"+ str(i) +"- ", result
    
#Fake some Misses
for i in range(100001,150000):
    result = mc.get("Test_Key_"+ str(i))
    print "Set: Test_Key_"+ str(i) +"- ", result