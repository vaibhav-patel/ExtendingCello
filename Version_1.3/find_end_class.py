
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
	while end not in visited:
		visited.add(end)
		nc=1
		#print end

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
