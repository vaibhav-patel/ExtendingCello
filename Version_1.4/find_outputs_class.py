def find_outputs(lines):
	outputs=[]
	count=0
	for idx,l in enumerate(lines):
		if 'Pin' in l:
			count=count+1
			if(count>2):	
				if 'output' in lines[idx+2]:
					outputs.append(l)
	total_outputs=len(outputs)
	outputs_dict={}
	outputs_pos_dict={}

	count=1
	for w in outputs:
		arr=w.split()
		x1=arr[2]
		lx1=len(x1)
		x1=x1[5:lx1-1]
		outputs_dict[x1]='op'+str(count)
		outputs_pos_dict['op'+str(count)]=x1
		count=count+1
	ret={}
	ret['a']=outputs_dict
	ret['b']=outputs_pos_dict

	return ret
