def quicksort(l):
	if len(l) >= 2:
		left = [x for x in l[1:] if x < l[0]]
		right = [x for x in l[1:] if x > l[0]]
		return quicksort(left) + [l[0]] + quicksort(right)
	elif len(l) <=1:
		return l

print quicksort([1,5,6,0,4])
print "hola"