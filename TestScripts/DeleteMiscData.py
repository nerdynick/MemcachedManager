import memcache

mc = memcache.Client(['127.0.0.1:11211','127.0.0.1:11212'], debug=0)
result = mc.delete("Test_Key_1")
print "Delete: Test_Key_1 - ", result

result = mc.delete("Test_Key_2")
print "Delete: Test_Key_2 - ", result

result = mc.delete("Test_Key_3")
print "Delete: Test_Key_3 - ", result

result = mc.delete("Test_Key_4")
print "Delete: Test_Key_4 - ", result

result = mc.delete("Test_Key_5")
print "Delete: Test_Key_5 - ", result

result = mc.delete("Test_Key_6")
print "Delete: Test_Key_6 - ", result

result = mc.delete("Test_Key_7")
print "Delete: Test_Key_7 - ", result

result = mc.delete("Test_Key_8")
print "Delete: Test_Key_8 - ", result