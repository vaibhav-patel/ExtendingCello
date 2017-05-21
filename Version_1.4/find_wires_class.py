
def find_wires(lines):
	wires=[]
	for l in lines:
		if 'wire' in l:
			wires.append(l)
	wire_dict1={}
	wire_dict2={}
	nodes=set()
	times={}
	for w in wires:
		arr=w.split()
		x1=arr[1]
		x2=arr[2]
		lx1=len(x1)
		lx2=len(x2)
		x1=x1[6:lx1-1]
		x2=x2[4:lx2-3]
		if(x1 in wire_dict1):
			if(x2 not in wire_dict1):
				wire_dict1[x2]=x1
			else:
				print 'danger'
		else:
			wire_dict1[x1]=x2
	return [wire_dict1]
