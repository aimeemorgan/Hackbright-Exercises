from sys import argv

script, filename = argv

scores = open(filename).read().split("\n")

restaurant_dict = {}

for item in scores:
	pair = item.split(":")
	restaurant_dict[pair[0]] = pair[1]

for item in sorted(restaurant_dict.items()):
	print "Restaurant " + item[0] + " is rated at %.1f." % float(item[1])


