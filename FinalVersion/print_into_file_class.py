import math
import numpy as np
from get_truth_table_class import get_truth_table
from assign_based_class import assign_based
def write_into_a_file(temp_string,fname):
	f = open(fname+'.verilog', 'w')
	f.write(temp_string)  # python will convert \n to os.linesep
	f.close()
	f = open(fname+'.HDL', 'w')
	f.write(temp_string)  # python will convert \n to os.linesep
	f.close()
	f = open(fname+'.txt', 'w')
	f.write(temp_string)  # python will convert \n to os.linesep
	f.close()

def plist(l):
	for i in l:
		print i


def print_into_file(fname,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,fname_vap):
	ffname=fname
	fname=fname.split('/')
	lfname=len(fname)
	fname=fname[lfname-1]
	str1='module '+fname+'('
	len_ops=len(ops)
	for i in range(len_ops):
		str1=str1+'output out'+str(i+1)+', '
	len_inputs=len(pins)
	str1=str1+'input '

	for i in range(len_inputs-1):
		str1=str1+'in'+str(i+1)+', '
	str1=str1+'in'+str(len_inputs)
	str1=str1+');\n'
#	print str1
	name={}
	available=[]
	count=0	
	for i in pins:
		available.append(i)
		count=count+1
		name[i]='in'+str(count)

	total=len(pins) + len(nots_end)+len(ands_end)+len(or_end)
	vap_count=1
	for i in ops:
		name[i]='out'+str(vap_count)
		vap_count=vap_count+1
#	print 'debug1'
	count=1
	while(len(available)>0):
		pin=available[0]
#		print 'hi'
#		print available
#		print 'hi'
		pin2=None
		save=None
		if(pin in connection_and.values()):
			for i in connection_and:
				if(connection_and[i]==pin):
					temp=i
					ltemp=len(temp)
					fl=2
					if('right' in temp):
						fl=0
						temp=temp[0:ltemp-5]
					if('left' in temp):
						fl=1
						temp=temp[0:ltemp-4]
					if(fl==0):
						vx1=connection_and[temp+'left']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(fl==1):
						vx1=connection_and[temp+'right']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin
#					print pin2

					str1=str1+'  and ('+name[temp]+', '+name[pin]+', '+name[pin2]+');\n'
					
					break
		if(pin in connection_or.values()):
			for i in connection_or:
				if(connection_or[i]==pin):
					temp=i
					ltemp=len(temp)
					fl=2
					if('right' in temp):
						fl=0
						temp=temp[0:ltemp-5]
					if('left' in temp):
						fl=1
						temp=temp[0:ltemp-4]
					if(fl==0):
						vx1=connection_or[temp+'left']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(fl==1):
						vx1=connection_or[temp+'right']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin
#					print pin2

					str1=str1+'  or ('+name[temp]+', '+name[pin]+', '+name[pin2]+');\n'
					

					break
			
		if(pin in connection_not.values()):
			for i in connection_not:
				if(connection_not[i]==pin):
					temp=i
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin

					str1=str1+'  not ('+name[temp]+', '+name[pin]+');\n'
					
					
					break
			
	



		if(save==None):
			f=1
		else:	
			available.append(save)		
		available.remove(pin)
		if(pin2==None):
			f=1
		else:
			available.remove(pin2)
	count=count-1
	str1=str1.split(';')
#	print str1
#	print 'debug2'
	str2='\n'
	str3=''
	lstr=len(str1)
	for idx,i in enumerate(str1[0:lstr-1]):
		if(idx==1):
			if(count>0):
				str2=str2+'  wire '
				for j in range(count-1):
					str2=str2+'w'+str(j+1)+', '
				str2=str2+'w'+str(count)	
				str2=str2+';'
				str3=str3+str2
		str3=str3+i+';'

	str3=str3+'\nendmodule;'
	if(fname_vap==2):
		str3=get_truth_table(str3,pins,ops)
		write_into_a_file(str3,ffname+'_truth_table_based')

	if(fname_vap==3):
		str3=assign_based(str3)
		write_into_a_file(str3,ffname+'_assign_based')
	if(fname_vap==1):
		write_into_a_file(str3,ffname+'_gate_based')

		
	return str3
#	print str3

#	print total
#	print pins
#	print connection_and
#	print connection_or
#	print connection_not

def write_that(temp,fname):
	f = open(fname, 'w')
	f.write(temp_string)  
	f.close()	

def write_into_a_file_parallel(temp_string,fname):
	p1 = Process(target=write_that, args=(temp_string,fname+'.verilog'))
	p1.start()
	p2 = Process(target=write_that, args=(temp_string,fname+'.HDL'))
	p2.start()
	p3 = Process(target=write_that, args=(temp_string,fname+'.txt'))
	p3.start()
	#top1=ansav['rt']
	p1.join()
	p2.join()
	p3.join()

def pragma_omp_parallel_for():
	p1 = Process(target=find_outputs, args=())
	p1.start()
	#top1=ansav['rt']
	p1.join()
	p2.join()
	p3.join()

def print_into_file_parallel(fname,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,fname_vap):
	ffname=fname
	fname=fname.split('/')
	lfname=len(fname)
	fname=fname[lfname-1]
	str1='module '+fname+'('
	len_ops=len(ops)
	pragma_omp_parallel_for()
	for i in range(len_ops):
		str1=str1+'output out'+str(i+1)+', '
	len_inputs=len(pins)
	str1=str1+'input '
	pragma_omp_parallel_for()
	for i in range(len_inputs-1):
		str1=str1+'in'+str(i+1)+', '
	str1=str1+'in'+str(len_inputs)
	str1=str1+');\n'
#	print str1
	name={}
	available=[]
	count=0	
	pragma_omp_parallel_for()
	for i in pins:
		available.append(i)
		count=count+1
		name[i]='in'+str(count)

	total=len(pins) + len(nots_end)+len(ands_end)+len(or_end)
	vap_count=1
	pragma_omp_parallel_for()
	for i in ops:
		name[i]='out'+str(vap_count)
		vap_count=vap_count+1
#	print 'debug1'
	count=1
	pragma_omp_parallel_for()
	while(len(available)>0):
		pin=available[0]
#		print 'hi'
#		print available
#		print 'hi'
		pin2=None
		save=None
		if(pin in connection_and.values()):
			pragma_omp_parallel_for()
			for i in connection_and:
				if(connection_and[i]==pin):
					temp=i
					ltemp=len(temp)
					fl=2
					if('right' in temp):
						fl=0
						temp=temp[0:ltemp-5]
					if('left' in temp):
						fl=1
						temp=temp[0:ltemp-4]
					if(fl==0):
						vx1=connection_and[temp+'left']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(fl==1):
						vx1=connection_and[temp+'right']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin
#					print pin2

					str1=str1+'  and ('+name[temp]+', '+name[pin]+', '+name[pin2]+');\n'
					
					break
		if(pin in connection_or.values()):
			pragma_omp_parallel_for()
			for i in connection_or:
				if(connection_or[i]==pin):
					temp=i
					ltemp=len(temp)
					fl=2
					if('right' in temp):
						fl=0
						temp=temp[0:ltemp-5]
					if('left' in temp):
						fl=1
						temp=temp[0:ltemp-4]
					if(fl==0):
						vx1=connection_or[temp+'left']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(fl==1):
						vx1=connection_or[temp+'right']
						if(vx1 not in name):
							continue
						pin2=vx1
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin
#					print pin2

					str1=str1+'  or ('+name[temp]+', '+name[pin]+', '+name[pin2]+');\n'
					

					break
			
		if(pin in connection_not.values()):
			pragma_omp_parallel_for()
			for i in connection_not:
				if(connection_not[i]==pin):
					temp=i
					if(temp not in name):
						save=temp
						name[temp]='w'+str(count)	
#						print temp
#						print name
						count=count+1	
#					print temp
#					print pin

					str1=str1+'  not ('+name[temp]+', '+name[pin]+');\n'					
					break

		if(save==None):
			f=1
		else:	
			available.append(save)		
		available.remove(pin)
		if(pin2==None):
			f=1
		else:
			available.remove(pin2)
	count=count-1
	str1=str1.split(';')
#	print str1
#	print 'debug2'
	str2='\n'
	str3=''
	lstr=len(str1)
	pragma_omp_parallel_for()

	for idx,i in enumerate(str1[0:lstr-1]):
		if(idx==1):
			if(count>0):
				str2=str2+'  wire '
				pragma_omp_parallel_for()
				for j in range(count-1):
					str2=str2+'w'+str(j+1)+', '
				str2=str2+'w'+str(count)	
				str2=str2+';'
				str3=str3+str2
		str3=str3+i+';'

	str3=str3+'\nendmodule;'
	if(fname_vap==2):
		str3=get_truth_table(str3,pins,ops)
		write_into_a_file(str3,ffname+'_truth_table_based')

	if(fname_vap==3):
		str3=assign_based(str3)
		write_into_a_file(str3,ffname+'_assign_based')
	if(fname_vap==1):
		write_into_a_file(str3,ffname+'_gate_based')
	
	return str3
#	print str3

def pragma_omp_parallel_for():
	p1 = Process(target=find_outputs, args=())
	p1.start()
	#top1=ansav['rt']
	p1.join()
	p2.join()
	p3.join()
