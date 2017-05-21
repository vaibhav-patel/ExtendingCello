import math
import numpy as np
def compute_tt(ins,s,w,lo1):
	ws=np.zeros((w,1),dtype=int)
	os=np.zeros((lo1,1),dtype=int)
	flos=np.zeros((lo1,1),dtype=int)
	#print w
	flag=np.zeros((w,1),dtype=int)
	ls=len(s)
	s=s[1:ls]
	for i in s:
		temp=i.split(' ')
		ltemp=len(temp)
		temp=temp[2:ltemp]
		#print temp
		#if('or' in i):
		if('or' in i):
			o1=temp[1]
			x1=temp[2]
			y1=temp[3]
			xorw1=0
			xorw2=0

			if('w' in x1):
				ii1=x1.index('w')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
#				print ii1	
#				print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=1

			if('in' in x1):
				ii1=x1.index('n')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
				#print ii1	
				#print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=2
			if('w' in y1):
				ii1=y1.index('w')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in x1):
					ii2=y1.index(')')
#				print ii1	
#				print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=1

			if('in' in y1):
				ii1=y1.index('n')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in y1):
					ii2=y1.index(')')
				#print ii1	
				#print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=2
			num1=num1-1
			num2=num2-1
			val1=-1
			if(xorw1==1):
				if(flag[num1]==1):
					val1=ws[num1,0]
			if(xorw1==2):
				val1=ins[num1]
			#print (val1,1)
			val2=-1
			if(xorw2==1):
				if(flag[num2]==1):
					val2=ws[num2,0]
			if(xorw2==2):
				val2=ins[num2]
			#print val2
			flo=0
			if('out' in o1):
				ii1=o1.index('t')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
				#print ii1	
				#print ii2
				num=o1[ii1+1:ii2]
				#print num
				num3=int(num)
				num3=num3-1
				flo=1
			if(flo==1):
				if(val1==1 or val2==1):
					if(flos[num3]==0):
						os[num3]=1
						flos[num3]=1
					else:
						print 'danger'
			if('w' in o1):
				ii1=o1.index('w')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
#				print ii1	
#				print ii2
				num=o1[ii1+1:ii2]
				#print num
				#print num
				num3=int(num)
				num3=num3-1
				if(val1==1 or val2==1):
					if(flag[num3]==0):
						ws[num3]=1
						flag[num3]=1
						tp=1
					else:
						print 'danger'
				else:
					if(flag[num3]==0):
						flag[num3]=1
					else:
						print 'danger2'

		if('and' in i):
			o1=temp[1]
			x1=temp[2]
			y1=temp[3]
			xorw1=0
			xorw2=0

			if('w' in x1):
				ii1=x1.index('w')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
#				print ii1	
#				print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=1

			if('in' in x1):
				ii1=x1.index('n')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
				#print ii1	
				#print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=2
			if('w' in y1):
				ii1=y1.index('w')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in x1):
					ii2=y1.index(')')
#				print ii1	
#				print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=1

			if('in' in y1):
				ii1=y1.index('n')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in y1):
					ii2=y1.index(')')
				#print ii1	
				#print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=2
			num1=num1-1
			num2=num2-1
			val1=-1
			if(xorw1==1):
				if(flag[num1]==1):
					val1=ws[num1,0]
			if(xorw1==2):
				val1=ins[num1]
			#print (val1,1)
			val2=-1
			if(xorw2==1):
				if(flag[num2]==1):
					val2=ws[num2,0]
			if(xorw2==2):
				val2=ins[num2]
			#print val2
			flo=0
			if('out' in o1):
				ii1=o1.index('t')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
				#print ii1	
				#print ii2
				num=o1[ii1+1:ii2]
				#print num
				num3=int(num)
				num3=num3-1
				flo=1
			if(flo==1):
				if(val1==1 and val2==1):
					if(flos[num3]==0):
						os[num3]=1
						flos[num3]=1
					else:
						print 'danger'
			if('w' in o1):
				ii1=o1.index('w')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
#				print ii1	
#				print ii2
				num=o1[ii1+1:ii2]
				#print num
				#print num
				num3=int(num)
				num3=num3-1
				if(val1==1 and val2==1):
					if(flag[num3]==0):
						ws[num3]=1
						flag[num3]=1
						tp=1
					else:
						print 'danger'
				else:
					if(flag[num3]==0):
						flag[num3]=1
					else:
						print 'danger2'

		#print ws
		if('not' in i):
			o1=temp[1]
			x1=temp[2]
			xorw1=0
			y1=x1

			if('w' in x1):
				ii1=x1.index('w')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
#				print ii1	
#				print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=1

			if('in' in x1):
				ii1=x1.index('n')
				if(',' in x1):
					ii2=x1.index(',')
				if(')' in x1):
					ii2=x1.index(')')
				#print ii1	
				#print ii2
				num=x1[ii1+1:ii2]
				#print num
				num1=int(num)
				xorw1=2
			if('w' in y1):
				ii1=y1.index('w')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in x1):
					ii2=y1.index(')')
#				print ii1	
#				print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=1

			if('in' in y1):
				ii1=y1.index('n')
				if(',' in y1):
					ii2=y1.index(',')
				if(')' in y1):
					ii2=y1.index(')')
				#print ii1	
				#print ii2
				num=y1[ii1+1:ii2]
				#print num
				num2=int(num)
				xorw2=2
			num1=num1-1
			val1=-1
			if(xorw1==1):
				if(flag[num1]==1):
					val1=ws[num1,0]
			if(xorw1==2):
				val1=ins[num1]
			#print (val1,1)
			flo=0
			if('out' in o1):
				ii1=o1.index('t')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
				#print ii1	
				#print ii2
				num=o1[ii1+1:ii2]
				#print num
				num3=int(num)
				num3=num3-1
				flo=1
			if(flo==1):
				if(val1==1):
					if(flos[num3]==0):
						os[num3]=0
						flos[num3]=1
					else:
						print 'danger'
				if(val1==0):
					if(flos[num3]==0):
						os[num3]=1
						flos[num3]=1
					else:
						print 'danger2'		
			if('w' in o1):
				ii1=o1.index('w')
				if(',' in o1):
					ii2=o1.index(',')
				if(')' in o1):
					ii2=o1.index(')')
#				print ii1	
#				print ii2
				num=o1[ii1+1:ii2]
				#print num
				#print num
				num3=int(num)
				num3=num3-1
				if(val1==1):
					if(flag[num3]==0):
						ws[num3]=0
						flag[num3]=1
						tp=1
					else:
						print 'danger'
				else:
					if(flag[num3]==0):
						ws[num3]=1
						flag[num3]=1
					else:
						print 'danger2'

	#plist(ws)
	#plist(os)
	#print ws
	#print os
	return os
















def get_truth_table(s,pins,outs):
	s=s.split('\n')
	fline=s[0]

	ls=len(s)
	s=s[1:ls-1]
	lp=len(pins)
	lo=len(outs)
	xx=int(math.pow(2,lp))
	matrix=np.zeros((xx,lp),dtype=int)
	matrix_out=np.zeros((xx,lo),dtype=int)
	for i in range(xx):
		str1="{0:b}".format(i)
		lstr1=len(str1)
		for j in range(lstr1):
			if(str1[lstr1-j-1]=='1'):
				matrix[i][lp-j-1]=int(1) 
	temp=s[0]
	temp=temp.split(',')
	ltemp=len(temp)
	for i in range(xx):
		temp=compute_tt(matrix[i,:],s,ltemp,lo)
		matrix_out[i,:]=temp
	#compute_tt(matrix[5,:],s,ltemp,lo)
	#print matrix_out
	'''
	module XOR(output out1, input in1, in2);
		always@(in1,in2)
		    begin
		      case({in1,in2})
		        2'b00: {out1} = 1'b0;
		        2'b01: {out1} = 1'b1;
		        2'b10: {out1} = 1'b1;
		        2'b11: {out1} = 1'b0;
		      endcase
		    end
		endmodule
	'''
	answer=''
	answer=answer+fline+'\n'
#	print answer
	temp=answer.split(' ')
	ltemp=len(temp)
	temp=temp[ltemp-lp: ltemp]
	xtemp=temp[lp-1]
	lxtemp=len(xtemp)
	xtemp=xtemp[0:lxtemp-2]
	temp[lp-1]=xtemp
	#plist(temp)
	sline=''
	sline=sline+'   always@('
	for i in temp:
		sline=sline+i
	answer=answer+ sline+'\n'
	answer=answer+'      begin\n'
	tline='         case({'
	for i in temp:
		tline=tline+i
	ltline=len(tline)
	tline=tline[0:ltline-1]+'})'
	answer=answer+tline+'\n'
	for i in range(xx):
		tempans='           '+str(lp)+'\'b'
		is1=''
		for j in range(lp):
			is1=is1+str(matrix[i][j])
		#print is1
		tempans=tempans+is1
		tempans=tempans+': {'
		for v in range(lo):
			tempans=tempans+'out' +str(v+1)+', '
		ltempans=len(tempans)
		tempans=tempans[0:ltempans-2]
		#print tempans
		tempans=tempans+'} = '+str(lo)+'\'b'
		os1=''
		for k in range(lo):
			os1=os1+str(matrix_out[i][k])
		tempans=tempans+os1
		tempans=tempans+';\n'
		answer=answer+tempans
	answer=answer+'         endcase\n'
	answer=answer+'      end\n'
	answer=answer+'endmodule\n'
	print answer






