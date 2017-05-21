import sys
from time import sleep
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QCheckBox, QWidget,QGridLayout,QLineEdit, QPushButton,QTextEdit, QFileDialog,QRadioButton,QHBoxLayout
import matplotlib.pyplot as plt
import networkx as nx
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
from subprocess import call
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math
import numpy as np
class filedialogdemo(QWidget):
	def __init__(self, parent = None):
		super(filedialogdemo, self).__init__(parent)

		layout = QGridLayout()
		self.resize(600, 600)
		variables=[]
		self.variables=variables
		dict1={}
		self.variables.append(dict1)
		xlayout=QGridLayout()
		layout.addLayout(xlayout,2,0)
		self.variables[0]['gogen']=0
		xlayout=QGridLayout()

		self.textbox4 = QLineEdit()
		self.textbox4.setReadOnly(True)
		self.textbox4.setText('Number of inputs')
		self.variables[0]['text']=''

		self.textbox5 = QLineEdit()
		self.textbox5.setReadOnly(True)
		self.textbox5.setText('Number of outputs')
		self.variables[0]['text']=''
		self.textbox6 = QLineEdit()
		self.textbox6.setReadOnly(True)
		self.textbox6.setText('File name')
		self.variables[0]['text']=''
		self.variables[0]['textbox']=1
		count=9
		xlayout.addWidget(self.textbox4,0,0)
		xlayout.addWidget(self.textbox5,0,1)
		xlayout.addWidget(self.textbox6,0,2)
		#      layout.addLayout(xlayout,0,0)


		self.textbox = QLineEdit()
		#      self.textbox.setReadOnly(True)
		self.textbox.setText('')
		self.variables[0]['text']=''

		self.textbox1 = QLineEdit()
		#      self.textbox.setReadOnly(True)
		self.textbox1.setText('')
		self.variables[0]['text']=''
		self.textbox2 = QLineEdit()
		#      self.textbox.setReadOnly(True)
		self.textbox2.setText('save as')
		self.variables[0]['text']=''
		self.variables[0]['textbox']=1
		count=9
		xlayout.addWidget(self.textbox,1,0)
		xlayout.addWidget(self.textbox1,1,1)
		xlayout.addWidget(self.textbox2,1,2)
		#     layout.addLayout(xlayout,1,0)
		self.btn = QPushButton("Go")
		self.btn.clicked.connect(self.makefive)
		self.btn2 = QPushButton("Generate file")
		self.btn2.clicked.connect(self.genfive)
		xlayout.addWidget(self.btn,2,0)
		xlayout.addWidget(self.btn2,2,1)
		layout.addLayout(xlayout,0,0)

		layout.setRowStretch(0,20)
		layout.setRowStretch(1,1)
		layout.setRowStretch(2,100)



		#layout.addLayout(xlayout,count,0)
		#xlayout.setRowStretch(0,1)
		#xlayout.setRowStretch(1,20000)

		count=count+1
		self.variables[0]['lo']=layout
		self.setLayout(layout)
		self.setWindowTitle("Cello GUI")

	def genfive(self):
		inps=self.inps1
		ops=self.ops1
		ti=int(math.pow(2,inps))	
		ttba=np.zeros((ti,ops))
		xx=ti
		matrix=np.zeros((ti,inps))
		for i in range(xx):
			str1="{0:b}".format(i)
			lstr1=len(str1)
			for j in range(lstr1):
				if(str1[lstr1-j-1]=='1'):
					matrix[i][inps-j-1]=int(1) 
		print matrix

		for i in range(ti):
			for j in range(ops):
				if(self.total[i][j].isChecked()==True):
					ttba[i][j]=1
		matrix_out=ttba				

		fname=self.textbox2.text()
		str1='module '+fname+'('
		len_ops=ops		
		for i in range(len_ops):
			str1=str1+'output out'+str(i+1)+', '
		len_inputs=inps
		str1=str1+'input '

		for i in range(len_inputs-1):
			str1=str1+'in'+str(i+1)+', '
		str1=str1+'in'+str(len_inputs)
		str1=str1+');'
		fline=str1

		answer=''
		answer=answer+fline+'\n'
		#	print answer
		temp=answer.split(' ')
		ltemp=len(temp)
		temp=temp[ltemp-inps: ltemp]
		xtemp=temp[inps-1]
		lxtemp=len(xtemp)
		xtemp=xtemp[0:lxtemp-2]
		temp[inps-1]=xtemp
		
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
			tempans='           '+str(inps)+'\'b'
			is1=''
			for j in range(inps):
				is1=is1+str(int(matrix[i][j]))
			#print is1
			tempans=tempans+is1
			tempans=tempans+': {'
			for v in range(ops):
				tempans=tempans+'out' +str(v+1)+', '
			ltempans=len(tempans)
			tempans=tempans[0:ltempans-2]
			#print tempans
			tempans=tempans+'} = '+str(ops)+'\'b'
			os1=''
			for k in range(ops):
				os1=os1+str(int(matrix_out[i][k]))
			tempans=tempans+os1
			tempans=tempans+';\n'
			answer=answer+tempans
		answer=answer+'         endcase\n'
		answer=answer+'      end\n'
		answer=answer+'endmodule\n'
		print answer


	def makefive(self):
		flag1=1
		flag2=1
		inps=self.textbox.text()
		try:
			flag1=1
			inps=int(inps)
			self.textbox.setText(str(inps))
			QApplication.processEvents()
		except:
			flag1=0
			self.textbox.setText('Make it an integer')
			QApplication.processEvents()
		ops=self.textbox1.text()
		try:
			flag2=1
			ops=int(ops)
			self.textbox1.setText(str(ops))
			QApplication.processEvents()
		except:
			flag2=0
			self.textbox1.setText('Make it an integer')
			QApplication.processEvents()

		if(flag1==1 and flag2==1):
			self.inps1=inps
			self.ops1=ops
			btnsl=[]
			po=int(math.pow(2,inps))
			self.arr = []
			self.total=[]
			for i in range(po):
				str1="{0:b}".format(i)
				tmp=QLineEdit()
				self.arr.append(tmp)
				self.arr[i].setReadOnly(True)
				lstr1=len(str1)
				ans=''
				for vap in range(lstr1,inps):
					ans=ans+'0  ||  '
				for q in str1:	
					ans=ans+q+'  ||  '
				lans=len(ans)
				ans=ans[0:lans-4]
				self.arr[i].setText(ans)
				tmp=[]							
				lo=self.layout()
				for j in range(ops):
					tmp.append(QCheckBox(str(j+1)))
				self.total.append(tmp)
				for j in range(ops):
					lo.addWidget(tmp[j],2+i,1+j)

				lo.addWidget(self.arr[i],2+i,0)
				btnsl.append(tmp)

   
         
   			
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()