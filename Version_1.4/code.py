from removekey_class import removekey
from find_wires_class import find_wires
from find_inputs_class import find_inputs
from find_outputs_class import find_outputs
from find_not_gates_class import find_not_gates
from find_and_gates_class import find_and_gates
from find_or_gates_class import find_or_gates
from give_methods_class import give_start_not
from give_methods_class import give_end_not
from give_methods_class import give_start_left_or
from give_methods_class import give_start_right_or
from give_methods_class import give_end_left_or
from give_methods_class import give_end_right_or
from find_end_class import find_end
from print_into_file_class import print_into_file

		




with open('example_circuits/easy.circ') as f:
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



#print pins
#print wires1
#print ops
#print nots_end
#print ands_end
#print or_end

inps=[]
for i in pins:
	inps.append(i)

intermediates_list=[]

connection_not={}
for i in nots_end:
	intermediates_list.append(i)
	connection_not[i]='empty'

connection_and={}
for i in ands_end:
	intermediates_list.append(i)
	connection_and[i+'left']='empty'
	connection_and[i+'right']='empty'

connection_or={}
for i in or_end:
	intermediates_list.append(i)
	connection_or[i+'left']='empty'
	connection_or[i+'right']='empty'

intermediates={}
for idx,i in enumerate(intermediates_list):
	intermediates[i]='w'+str(idx+1)


while (len(inps)>0):
	curr=inps[0]
	end=find_end(curr,wires1)

	orl_end=give_end_left_or(end)
	orr_end=give_end_right_or(end)
	end_not=give_end_not(end)
#	print (curr, end)
	if (orl_end in or_end ):	
		connection_or[orl_end+'left']=curr
#		print 'or left'
		if (orl_end not in inps):
			inps.append(orl_end)
	if(orr_end in or_end):
		connection_or[orr_end+'right']=curr
#		print 'or right'
		if (orr_end not in inps):
			inps.append(orr_end)	
	if(orl_end in ands_end):
#		print 'and left'
		connection_and[orl_end+'left']=curr
		if (orl_end not in inps):
			inps.append(orl_end)
	if(orr_end in ands_end):
#		print 'and right'
		connection_and[orr_end+'right']=curr		
		if (orr_end not in inps):
			inps.append(orr_end)
	if(end_not in nots_end):
#		print 'not gate'
		connection_not[end_not]=curr
		if (end_not not in inps):
			inps.append(end_not)
#	if(end in ops):
#		print 'output pin'
	inps.remove(curr)


'''
module XOR(output out1,  input in1, in2);
  wire w1, w2, w3, w4;
  not (w1, in1);
  not (w2, in2);
  not (w3, in1, w2);
  not (w4, in2, w1);
  or (out1, w3, w4);
endmodule
'''

#print 'connections'
#print 'connections not'

#print connection_not
#print 'connections and'
#for i in connection_and:
#	print (i,connection_and[i])

#print 'connections or'
#for i in connection_or:
#	print (i,connection_or[i])

ops_end={}
for i in ops:
	temp=find_end(i,wires1)
	ops_end[i]=temp
for i in ops:
	temp=ops_end[i]
	if(temp+'right' in connection_and):
		x1=connection_and[temp+'right']
		x2=connection_and[temp+'left']
		connection_and.pop(temp+'right', None)
		connection_and.pop(temp+'left', None)
		connection_and[i+'right']=x1
		connection_and[i+'left']=x2

for i in ops:
	temp=ops_end[i]
	if(temp+'right' in connection_or):
		x1=connection_or[temp+'right']
		x2=connection_or[temp+'left']
		connection_or.pop(temp+'right', None)
		connection_or.pop(temp+'left', None)
		connection_or[i+'right']=x1
		connection_or[i+'left']=x2

for i in ops:
	temp=ops_end[i]
	if(temp in connection_not):
		x1=connection_not[temp]
		connection_not.pop(temp, None)
		connection_not[i]=x1
		
#print 'connections'
#print 'connections not'

#print connection_not
#print 'connections and'
#for i in connection_and:
#	print (i,connection_and[i])

#print 'connections or'
#for i in connection_or:
#	print (i,connection_or[i])


print_into_file('output/first_file',ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not)



