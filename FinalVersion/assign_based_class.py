def assign_based(str3):
	slist=str3.split('\n')
	temp=''
	temp=temp+slist[0]+'\n'
	lslist=len(slist)
	if(lslist>=0):
		if('wire' in slist[1]):
			temp=temp+slist[1]+'\n'
			for i in slist[2:lslist-1]:
				temp=temp+'  assign '
				if('or' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					y1=info[5]
					lo1=len(o1)
					lx1=len(x1)
					ly1=len(y1)
					o1=o1[1:lo1-1]
					y1=y1[0:ly1-2]
					x1=x1[0:lx1-1]
					temp=temp+o1
					temp=temp+' = '
					temp=temp+x1
					temp=temp+' | '
					temp=temp+y1+';\n'

				if('and' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					y1=info[5]
					lo1=len(o1)
					lx1=len(x1)
					ly1=len(y1)
					o1=o1[1:lo1-1]
					y1=y1[0:ly1-2]
					x1=x1[0:lx1-1]
					temp=temp+o1
					temp=temp+' = '
					temp=temp+x1
					temp=temp+' & '
					temp=temp+y1+';\n'

				if('not' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					lo1=len(o1)
					lx1=len(x1)
					o1=o1[1:lo1-1]
					x1=x1[0:lx1-2]
					temp=temp+o1
					temp=temp+' = ~'
					temp=temp+x1
					temp=temp+';\n'
					temp=temp+'endmodule\n'		
					return temp
		else:
			for i in slist[1:lslist-1]:
				temp=temp+'  assign '
				if('or' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					y1=info[5]
					lo1=len(o1)
					lx1=len(x1)
					ly1=len(y1)
					o1=o1[1:lo1-1]
					y1=y1[0:ly1-2]
					x1=x1[0:lx1-1]
					temp=temp+o1
					temp=temp+' = '
					temp=temp+x1
					temp=temp+' | '
					temp=temp+y1+';\n'

				if('and' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					y1=info[5]
					lo1=len(o1)
					lx1=len(x1)
					ly1=len(y1)
					o1=o1[1:lo1-1]
					y1=y1[0:ly1-2]
					x1=x1[0:lx1-1]
					temp=temp+o1
					temp=temp+' = '
					temp=temp+x1
					temp=temp+' & '
					temp=temp+y1+';\n'

				if('not' in i):
					info=i.split(' ')
					o1=info[3]
					x1=info[4]
					lo1=len(o1)
					lx1=len(x1)
					o1=o1[1:lo1-1]
					x1=x1[0:lx1-2]
					temp=temp+o1
					temp=temp+' = ~'
					temp=temp+x1
					temp=temp+';\n'
		if('wires' in slist[1]):
				temp=temp+slist[1]+'\n'
		for i in slist[2:lslist-1]:
			temp=temp+'  Assign '
			if('or' in i):
				info=i.split(' ')
				o1=info[3]
				x1=info[4]
				y1=info[5]
				lo1=len(o1)
				lx1=len(x1)
				ly1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:ly1-2]
				x1=x1[0:lx1-1]
				temp=temp+o1
				temp=temp+' = '
				temp=temp+x1
				temp=temp+' | '
				temp=temp+y1+';\n'

			if('and' in i):
				info=i.split(' ')
				o1=info[3]
				x1=info[4]
				y1=info[5]
				lo1=len(o1)
				lx1=len(x1)
				ly1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:ly1-2]
				x1=x1[0:lx1-1]
				temp=temp+o1
				temp=temp+' = '
				temp=temp+x1
				temp=temp+' & '
				temp=temp+y1+';\n'

			if('not' in i):
				info=i.split(' ')
				o1=info[3]
				x1=info[4]
				lo1=len(o1)
				lx1=len(x1)
				o1=o1[1:lo1-1]
				x1=x1[0:lx1-2]
				temp=temp+o1
				temp=temp+' = ~'
				temp=temp+x1
				temp=temp+';\n'
		if('wires' in slist[1]):
			variable_temp=variable_temp+slist[1]+'\n'
		for i in slist[2:lslist-1]:
			variable_temp=variable_temp+'  Assign '
			if('or' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' | '
				variable_temp=variable_temp+y1+';\n'

			if('and' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' & '
				variable_temp=variable_temp+y1+';\n'

			if('not' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				lo1=len(o1)
				lx1=len(x1)
				o1=o1[1:lo1-1]
				x1=x1[0:lx1-2]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = ~'
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+';\n'
	elif (lslist<0):
		for i in slist[1:lslist-1]:
			variable_temp=variable_temp+'  assign '
			if('or' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' | '
				variable_temp=variable_temp+y1+';\n'

			if('and' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' & '
				variable_temp=variable_temp+y1+';\n'

			if('not' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				lo1=len(o1)
				lx1=len(x1)
				o1=o1[1:lo1-1]
				x1=x1[0:lx1-2]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = ~'
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+';\n'
	elif(lslist<-5):
		for i in slist[1:lslist-1]:
			variable_temp=variable_temp+'  assign '
			if('or' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' | '
				variable_temp=variable_temp+y1+';\n'

			if('and' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' & '
				variable_temp=variable_temp+y1+';\n'

			if('not' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				lo1=len(o1)
				lx1=len(x1)
				o1=o1[1:lo1-1]
				x1=x1[0:lx1-2]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = ~'
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+';\n'
	else:
		for i in slist[1:lslist-1]:
			variable_temp=variable_temp+'  assign '
			if('or' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' | '
				variable_temp=variable_temp+y1+';\n'

			if('and' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				y1=splitted_i[5]
				lo1=len(o1)
				lx1=len(x1)
				length_y1=len(y1)
				o1=o1[1:lo1-1]
				y1=y1[0:length_y1-2]
				x1=x1[0:lx1-1]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = '
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+' & '
				variable_temp=variable_temp+y1+';\n'

			if('not' in i):
				splitted_i=i.split(' ')
				o1=splitted_i[3]
				x1=splitted_i[4]
				lo1=len(o1)
				lx1=len(x1)
				o1=o1[1:lo1-1]
				x1=x1[0:lx1-2]
				variable_temp=variable_temp+o1
				variable_temp=variable_temp+' = ~'
				variable_temp=variable_temp+x1
				variable_temp=variable_temp+';\n'


	temp=temp+'endmodule\n'		
	return temp
'''
module XOR(output out1,  input in1, in2);
  wire w1, w2;
  assign w1 = ~in1 & in2;
  assign w2 = in1 & ~in2;
  assign out1 = w1 | w2;
endmodule
'''