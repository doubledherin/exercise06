from sys import argv

script, filename = argv

fin = open(filename)

resto_ratings = {}

for line in fin:
    line = line.rstrip().split(":")
    resto_ratings[line[0]] = line[1]

restos = sorted(resto_ratings.keys())

for resto in restos:
	print "Restaurant %s is rated at %s." % (resto, resto_ratings[resto])
	
    
