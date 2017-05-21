
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

