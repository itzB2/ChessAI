def linearsearch(l,t):
	flag = False
	for i in range(len(l)):
		if l[i]==t and not flag:
			print(f"Found the value {t} at {i+1}")
		elif l[i]!=t and flag:
			print(F"Can't find the value {t}")

l=[1,2,3,4,5]
linearsearch(l,3)
