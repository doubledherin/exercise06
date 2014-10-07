
# states = {
#     "Oregon" :  "OR",
#     "Florida" : "FL",
#     "California" :"CA",
#     "New York" : "NY",
#     "Michigan" : "MI"
# }

# cities = {
#     "CA" : "San Francisco",
#     "MI" : "Detroit",
#     "FL" : "Jacksonville",
# }

# cities ["NY"] = "New York"
# cities ["OR"] = "Portland"

# print"-" * 10
# print "Michigan's abbreviation is: ", states ["Michigan"]
# print "Florida's abbreviation is: ", states["Florida"]

# print "-" *10
# print "Michigan has: ", cities[states["Michigan"]]
# print "Florida has: ", cities[states["Florida"]]

# print "-" *10
# for state, abbrev in states.items():
#     print "%s is abbreviated %s" % (state, abbrev)

# print "-" *10
# for abbrev, city in cities.items():
#     print "%s has the city %s" %(abbrev, city)

# print"-" *10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

# print "-" * 10
# state = states.get("Texas")

# if not state:
#     print "Sorry, no Texas."

# city = cities.get("TX","Does Not Exist")
# print "The city for the state 'TX' is: %s" % city

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()


