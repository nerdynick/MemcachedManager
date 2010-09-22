import memcache

mc = memcache.Client(['127.0.0.1:11211','127.0.0.1:11212'], debug=0)
results = mc.get_stats()
for result in results:
    print result[0]
    for key in result[1]:
        print "\t", key, "\t", result[1][key]