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

from multiprocessing import Process

def find_and_gates_parallel():
	nots=[]
	count=0
	lines=''
	pragma_omp_parallel_for()
	for l in lines:
		if 'AND' in l:
			count=count+1
			if(count>=2):
				nots.append(l)
	not_end=[]
	count=0
	pragma_omp_parallel_for()
	for w in nots:
		arr=w.split()
		x1=arr[2]
		lx1=len(x1)
		x1=x1[5:lx1-1]
		count=1
		not_end.append(x1)
	return not_end

def pragma_omp_parallel_for():
	p1 = Process(target=find_and_gates_parallel, args=())
	p1.start()
	#top1=ansav['rt']
	p2 = Process(target=find_and_gates_parallel, args=())
	p2.start()
	#top1=ansav['rt']
	p3 = Process(target=find_and_gates_parallel, args=())
	p3.start()
	#top1=ansav['rt']

	p1.join()
	p2.join()
	p3.join()
