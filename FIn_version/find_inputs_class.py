
def find_inputs(lines):
	inputs=[]
	count=0
	for idx,l in enumerate(lines):
		if 'Pin' in l:
			count=count+1
			if(count>2):	
				if 'tristate' in lines[idx+1]:
					inputs.append(l)
	total_inputs=len(inputs)
	inputs_dict={}
	inputs_pos_dict={}

	count=1
	for w in inputs:
		arr=w.split()
		#print arr
		x1=arr[2]
		lx1=len(x1)
		x1=x1[5:lx1-1]
		inputs_dict[x1]='pin'+str(count)
		inputs_pos_dict['pin'+str(count)]=x1
		count=count+1
	ret={}
	ret['a']=inputs_dict
	ret['b']=inputs_pos_dict

	return ret
