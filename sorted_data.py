from sys import argv

script, filename = argv

restaurant_raw = open(filename)

restos = []
scores = []

for line in restaurant_raw:
    line = line.rstrip().split(":")
    restos.append(line[0]) 
    scores.append(line[1])

# print restos
# print scores


rest_scores = zip(restos,scores)


sorted_rest_scores = sorted(rest_scores)

print sorted_rest_scores

for item in sorted_rest_scores:
    print "Restaurant %s is rated at %s." % (item[0], item[1])

    
