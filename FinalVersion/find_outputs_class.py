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
from multiprocessing import Process
def pragma_omp_parallel_for():
	p1 = Process(target=find_outputs, args=())
	p1.start()
	#top1=ansav['rt']
	p2 = Process(target=find_outputs, args=())
	p2.start()
	#top1=ansav['rt']
	p3 = Process(target=find_outputs, args=())
	p3.start()
	#top1=ansav['rt']

	p1.join()
	p2.join()
	p3.join()
