def find_and_gates(lines):
	nots=[]
	count=0
	for l in lines:
		if 'AND' in l:
			count=count+1
			if(count>=2):
				nots.append(l)
	not_end=[]
	count=0
	for w in nots:
		arr=w.split()
		x1=arr[2]
		lx1=len(x1)
		x1=x1[5:lx1-1]
		count=1
		not_end.append(x1)
	return not_end
