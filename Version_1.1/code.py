def removekey(d, key):
    r = dict(d)
    del r[key]
    return r





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


def find_not_gates(lines):
	nots=[]
	count=0
	for l in lines:
		if 'NOT' in l:
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

def find_or_gates(lines):
	nots=[]
	count=0
	for l in lines:
		if 'OR' in l:
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

def give_start_not(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])-30
	num2=x1[1]
	x2='('+str(num1)+','+str(num2)+')'
	return x2

def give_end_not(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])+30
	num2=x1[1]
	x2='('+str(num1)+','+str(num2)+')'
	return x2


def give_start_left_or(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])-50
	num2=int(x1[1])-20
	x2='('+str(num1)+','+str(num2)+')'
	return x2

def give_start_right_or(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])-50
	num2=int(x1[1])+20
	x2='('+str(num1)+','+str(num2)+')'
	return x2


def give_end_left_or(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])+50
	num2=int(x1[1])+20
	x2='('+str(num1)+','+str(num2)+')'
	return x2

def give_end_right_or(x1):
	lx1=len(x1)
	x1=x1[1:lx1-1]
	x1=x1.split(',')
	num1=int(x1[0])+50
	num2=int(x1[1])-20
	x2='('+str(num1)+','+str(num2)+')'
	return x2





def find_end(c,w1):
	visited=set()
	visited.add(c)
	if (c in w1):
		end=w1[c]
	else:
		for i in w1:
			if(w1[i]==c):
				end=i	
	##print c			
	#print end
#	raw_input()
	nc=1
	while end not in visited:
		visited.add(end)
		nc=1

		curr=end
		fl=0
		if curr in w1:
	#		print 'd1'
	#		print visited
	#		print curr
	#		print w1[curr]

	#		print 'd2'
			if w1[curr] not in visited:
				end=w1[curr]
				fl=1
				nc=0
	#			print 'i1'
		if fl==0:
	#		print 'i2'
			for i in w1:
	#			print i
				if(i not in visited):
					if(w1[i]==curr):
						end=i
	#					print 'i3'	
						nc=0

						break
		if(nc==1):
			break
	#	print end
	#	print visited
	#	print w1
	#	print curr
	#	raw_input()
	return end


		




with open('full.circ') as f:
    lines_global = f.read().splitlines()

wires_list=find_wires(lines_global)
wires1=wires_list[0]


ret=find_inputs(lines_global)
pins=ret['a']
pins_pos=ret['b']


ret=find_outputs(lines_global)
ops=ret['a']
ops_pos=ret['b']

nots_end=find_not_gates(lines_global)
ands_end=find_and_gates(lines_global)
or_end=find_or_gates(lines_global)



print pins
print wires1
print ops
print nots_end
print ands_end
print or_end

inps=[]
for i in pins:
	inps.append(i)
while (len(inps)>0):
	curr=inps[0]
	end=find_end(curr,wires1)

	orl_end=give_end_left_or(end)
	orr_end=give_end_right_or(end)
	end_not=give_end_not(end)

	print (curr, end)
	if (orl_end in or_end ):
		print 'or left'
	if(orr_end in or_end):
		print 'or right'
	
	if(orl_end in ands_end):
		print 'and left'
	if(orr_end in ands_end):
		print 'and right'
	if(end_not in nots_end):
		print 'not gate'

	inps.remove(curr)








