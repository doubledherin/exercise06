from sys import argv

script, filename = argv

fin = open(filename)

resto_ratings = {}

for line in fin:
    line = line.rstrip().split(":")
    resto_ratings[line[0]] = line[1]

print resto_ratings


#for item in sorted_rest_scores:
 #   print "Restaurant %s is rated at %s." % (item[0], item[1])

    
