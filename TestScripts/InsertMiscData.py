import memcache
import cStringIO

mc = memcache.Client(['127.0.0.1:11211','127.0.0.1:11212'], debug=0)

for i in range(1,10000):
    value = cStringIO.StringIO()
    for h in range(100):
        value.write("Test_Key_"+ str(i) +"_Value")
    result = mc.set("Test_Key_"+ str(i), value.getvalue())
    #print "Set: Test_Key_"+ str(i) +"- ", result