
# ages = {
# 		"Mike" : 34,
# 		"Jimothy" : 6,
# 		"Prometheus" : "Really Old"
# 		}
	
# print(ages["Mike"])


# for key in ages: 
# 	print(ages[key])

# for v in ages.values():
# 	print(v)



def getLetterCounts(s):
	d = dict()
	for c in s:
		if c.isalpha():
			c = c.lower()
			# if c in d:
			# 	d[c] += 1
			# else:
			# 	d[c] = 1
			d[c] = d.get(c,0) + 1

	return d

d = getLetterCounts("Kimchee is hungry")
print(d)