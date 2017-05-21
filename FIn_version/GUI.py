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
from multiprocessing import Process
import os
import sys
from multiprocessing import Pool

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QGridLayout()
      self.btn = QPushButton("Make a new circuit")
      self.btn.clicked.connect(self.makeanewexec)
      self.resize(600, 600)
      variables=[]
      self.variables=variables
      dict1={}
      self.variables.append(dict1)
      xlayout=QGridLayout()
      layout.addLayout(xlayout,2,0)
      self.variables[0]['gogen']=0



      self.btn1 = QPushButton("Load existing circ file")
      self.btn1.clicked.connect(self.loadexisting)
      xlayout.addWidget(self.btn,0,0)
      xlayout.addWidget(self.btn1,0,1)
      self.btnclr = QPushButton("Clear")
      self.btnclr.clicked.connect(self.clearbtn)
      self.btnclr.setStyleSheet('QPushButton {background-color: red;}')

      self.btnum = QPushButton("User Manual")
      self.btnum.clicked.connect(self.um)
      self.btnum.setStyleSheet('QPushButton {background-color: yellow;}')

      self.b1 = QRadioButton("Display all")
      self.b1.setChecked(True)
      self.b1.toggled.connect(lambda:self.btnstate1())
      xlayout.addWidget(self.b1,0,2)
      xlayout.addWidget(self.btnclr,0,3)
      xlayout.addWidget(self.btnum,0,4)
      xlayout.setColumnStretch(0,1.5)
      xlayout.setColumnStretch(1,4)
      xlayout.setColumnStretch(1,1)


      xlayout=QGridLayout()
      layout.addLayout(xlayout,3,0)      

      self.btn3 = QPushButton("Show wires")
      self.btn3.clicked.connect(self.show_wires)
      xlayout.addWidget(self.btn3,0,0)


      self.btn4 = QPushButton("Show Inputs")
      self.btn4.clicked.connect(self.show_inputs)
      xlayout.addWidget(self.btn4,0,1)
      

      self.btn5 = QPushButton("Show Outputs")
      self.btn5.clicked.connect(self.show_outputs)
      xlayout.addWidget(self.btn5,0,2)
      

      xlayout=QGridLayout()
      layout.addLayout(xlayout,4,0)      

      self.ppinp1 = QLineEdit('Number of processors')
      self.ppinp1.setReadOnly(True)
      xlayout.addWidget(self.ppinp1,0,0)
      
      self.ppinp = QLineEdit()
      #self.btn3.clicked.connect(self.show_wires)
      xlayout.addWidget(self.ppinp,0,1)


      self.ppchb = QCheckBox('Run with multiple processor')
      #self.btn4.clicked.connect(self.show_inputs)
      xlayout.addWidget(self.ppchb,0,2)
      
      xlayout=QGridLayout()
      layout.addLayout(xlayout,6,0)      

      self.btn6 = QPushButton("Show Gates")
      self.btn6.clicked.connect(self.show_gates)
      self.btn7 = QPushButton("Show AND Gates")
      self.btn7.clicked.connect(self.show_and)
      self.btn8 = QPushButton("Show OR Gates")
      self.btn8.clicked.connect(self.show_or)
      self.btn9 = QPushButton("Show NOT Gates")
      self.btn9.clicked.connect(self.show_not)
      xlayout.addWidget(self.btn6,0,0)      
      xlayout.addWidget(self.btn7,0,1)      
      xlayout.addWidget(self.btn8,0,2)      
      xlayout.addWidget(self.btn9,0,3)      
      
      self.btn2 = QPushButton("Generate virtual graph")
      self.btn2.clicked.connect(self.generatevirtualgraph)
      layout.addWidget(self.btn2)
      self.textbox1 = QLineEdit()
#     self.textbox.setReadOnly(True)
      self.textbox1.setText('Save as')
      self.variables[0]['saveas']=''
 
      layout.addWidget(self.textbox1)

      self.btngb = QPushButton("Gate based verilog")
      self.btngb.clicked.connect(self.gatebased)
      layout.addWidget(self.btngb)

      self.btngb2 = QPushButton("Truth Table based verilog")
      self.btngb2.clicked.connect(self.ttbased)
      layout.addWidget(self.btngb2)

      self.btngb3 = QPushButton("Assign based verilog")
      self.btngb3.clicked.connect(self.abased)
      layout.addWidget(self.btngb3)
      
      self.btngb4 = QPushButton("Give a truth table input")
      self.btngb4.clicked.connect(self.ttmake)
      layout.addWidget(self.btngb4)

      self.btngb4.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

      self.btnca = QPushButton("Compute all the three parallelly")
      self.btnca.clicked.connect(self.camake)
      layout.addWidget(self.btnca)

      self.btnca.setStyleSheet('QPushButton {background-color: #A3C111; color: red;}')

      xlayout=QGridLayout()

      self.textbox = QTextEdit()
      self.textbox.setReadOnly(True)
      self.textbox.setText('')
      self.variables[0]['text']=''
      self.variables[0]['textbox']=1
      count=9
      layout.addWidget(self.textbox)
      #layout.addLayout(xlayout,count,0)
      #xlayout.setRowStretch(0,1)
      #xlayout.setRowStretch(1,20000)

      count=count+1      

      self.setLayout(layout)
      self.setWindowTitle("Cello GUI")

   def makeanewexec(self):
      call(['java', '-jar', 'logisim.jar'])
   def um(self):
   	  call(['evince',  'userManual.pdf'])   

   def clearbtn(self):
      self.variables[0]['text']=''
      self.textbox.setText(self.variables[0]['text'])

   def generatevirtualgraph(self):
      try:
         #### for making the user interface smooth
         self.variables[0]['text']='Processing and generating virtual graphs using the canvas information'
         self.textbox.setText(self.variables[0]['text'])
         QApplication.processEvents()         
         timesleep=1.0
         divide=1.0
         if(self.ppchb.isChecked()):
            divide=float(self.ppinp.text())
         sleep(timesleep/divide)
         pins=self.variables[0]['pins']
         ands_end=self.variables[0]['ands_end']
         or_end=self.variables[0]['or_end']
         nots_end=self.variables[0]['nots_end']
         ops=self.variables[0]['ops']
         wires1=self.variables[0]['wires1']


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
         #  print (curr, end)
            if (orl_end in or_end ):   
               connection_or[orl_end+'left']=curr
         #     print 'or left'
               if (orl_end not in inps):
                  inps.append(orl_end)
            if(orr_end in or_end):
               connection_or[orr_end+'right']=curr
         #     print 'or right'
               if (orr_end not in inps):
                  inps.append(orr_end) 
            if(orl_end in ands_end):
         #     print 'and left'
               connection_and[orl_end+'left']=curr
               if (orl_end not in inps):
                  inps.append(orl_end)
            if(orr_end in ands_end):
         #     print 'and right'
               connection_and[orr_end+'right']=curr      
               if (orr_end not in inps):
                  inps.append(orr_end)
            if(end_not in nots_end):
         #     print 'not gate'
               connection_not[end_not]=curr
               if (end_not not in inps):
                  inps.append(end_not)
         #  if(end in ops):
         #     print 'output pin'
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
         #  print (i,connection_and[i])

         #print 'connections or'
         #for i in connection_or:
         #  print (i,connection_or[i])

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
         self.variables[0]['ca']=connection_and      
         self.variables[0]['co']=connection_or      
         self.variables[0]['cn']=connection_not      
         #print 'connections'
         #print 'connections not'

         #print connection_not
         #print 'connections and'
         #for i in connection_and:
         #  print (i,connection_and[i])

         #print 'connections or'
         #for i in connection_or:
         #  print (i,connection_or[i])
         self.variables[0]['gogen']=1
         ts='Producing generated results\n'
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)

         self.variables[0]['text']=ts
         self.textbox.setText(self.variables[0]['text'])
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'########             ----Connections----                ########\n'
         str1=str1+'######################################\n\n'

         str1=str1+'######################################\n'
         str1=str1+'########               AND connections                ########\n'
         str1=str1+'######################################\n'
         for idx,i in enumerate(connection_and):
            str1=str1+'And connection no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+' with '+connection_and[i]+' \n'
         str1=str1+'######################################\n'
         str1=str1+'###########               AND ends            ###########\n'
         str1=str1+'######################################\n\n\n'

         str1=str1+'######################################\n'
         str1=str1+'########               OR connections                ########\n'
         str1=str1+'######################################\n'
         for idx,i in enumerate(connection_or):
            str1=str1+'And connection no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+' with '+connection_or[i]+' \n'
         str1=str1+'######################################\n'
         str1=str1+'###########               OR ends            ###########\n'
         str1=str1+'######################################\n\n\n'

         str1=str1+'######################################\n'
         str1=str1+'########               NOT connections                ########\n'
         str1=str1+'######################################\n'
         for idx,i in enumerate(connection_not):
            str1=str1+'And connection no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+' with '+connection_not[i]+' \n'
         str1=str1+'######################################\n'
         str1=str1+'###########               NOT ends            ###########\n'
         str1=str1+'######################################\n\n\n'
         self.variables[0]['text']=str1
         self.textbox.setText(self.variables[0]['text'])

      except:
         self.variables[0]['text']='Please Select A CIRC FILE First'
         self.textbox.setText(self.variables[0]['text'])


   def show_wires(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)

         wires1=self.variables[0]['wires1']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########               Wires starts             #########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'Wire no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########               Wires ends             #########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            str2=self.variables[0]['text']+str1
            self.variables[0]['text']=str2
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No Wires Found)'
         self.textbox.setText(self.variables[0]['text'])


   def show_inputs(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         wires1=self.variables[0]['pins']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             Input pins starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'Input no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             Input pins ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            str2=self.variables[0]['text']+str1
            self.variables[0]['text']=str2
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No Input pins Found)'
         self.textbox.setText(self.variables[0]['text'])

   def show_outputs(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         wires1=self.variables[0]['ops']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             Output pins starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'Output no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             Output pins ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            str2=self.variables[0]['text']+str1
            self.variables[0]['text']=str2
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No Output pins Found)'
         self.textbox.setText(self.variables[0]['text'])

   def show_gates(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         wires1=self.variables[0]['ands_end']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             AND gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'AND gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             AND gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
#         self.textbox.setText(str1)
         wires1=self.variables[0]['or_end']
         data=wires1
         str1=str1+'######################################\n'
         str1=str1+'###########             OR gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'OR gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             OR gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
#         self.textbox.setText(str1)
         wires1=self.variables[0]['nots_end']
         data=wires1
         str1=str1+'######################################\n'
         str1=str1+'###########             NOT gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'NOT gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             NOT gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No Gates Found)'
         self.textbox.setText(self.variables[0]['text'])
   def show_and(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         wires1=self.variables[0]['ands_end']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             AND gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'AND gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             AND gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No AND gates)'
         self.textbox.setText(self.variables[0]['text'])
   def show_or(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         str1=''
         wires1=self.variables[0]['or_end']
         data=wires1
         str1=str1+'######################################\n'
         str1=str1+'###########             OR gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'OR gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             OR gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No OR gates)'
         self.textbox.setText(self.variables[0]['text'])
   def show_not(self):
      try:
         ts=''
         for vi in range(100):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         wires1=self.variables[0]['nots_end']
         data=wires1
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             NOT gates starts             ########\n'
         str1=str1+'######################################\n'

         for idx,i in enumerate(data):
            str1=str1+'NOT gate no. '
            str1=str1+str(idx+1)
            str1=str1+' at the position '
            str1=str1+i+'\n'
         str1=str1+'######################################\n'
         str1=str1+'###########             NOT gates ends             ########\n'
         str1=str1+'######################################\n\n\n'
         if(self.variables[0]['textbox']==1):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])
         elif(self.variables[0]['textbox']==0):
            self.variables[0]['text']=str1
            self.textbox.setText(self.variables[0]['text'])         
#         self.textbox.setText(str1)
      except:
         self.variables[0]['text']='Please Select A CIRC FILE (No NOT gates)'
         self.textbox.setText(self.variables[0]['text'])

   def loadexisting(self):
      fname = QFileDialog.getOpenFileName(self, 'Open file', 
         '/home',"CIRC files (*.circ)")
      with open(fname[0]) as f:
         lines_global = f.read().splitlines()
      #lines_global = fname.read().splitlines()
      self.variables[0]['lines_all']=lines_global

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
      self.variables[0]['wires1']=wires1
      self.variables[0]['pins']=pins
      self.variables[0]['ops']=ops
      self.variables[0]['nots_end']=nots_end
      self.variables[0]['ands_end']=ands_end
      self.variables[0]['or_end']=or_end


   def btnstate1(self):
      if(self.b1.isChecked()):
         self.variables[0]['textbox']=1
      else:
         self.variables[0]['textbox']=0


   def gatebased(self):
      try:
         if(self.variables[0]['gogen']==0):
            self.generatevirtualgraph()                 

         fname1=self.textbox1.text()
         pins=self.variables[0]['pins']
         ands_end=self.variables[0]['ands_end']
         or_end=self.variables[0]['or_end']
         nots_end=self.variables[0]['nots_end']
         ops=self.variables[0]['ops']
         wires1=self.variables[0]['wires1']
         connection_and=self.variables[0]['ca']
         connection_or=self.variables[0]['co']
         connection_not=self.variables[0]['cn']
         top=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,1)

         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########             Gate based Verilog             ########\n'
         str1=str1+'######################################\n'
         ts='Finding the order of gates for verilog file\n'
         for vi in range(200):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         str1=str1+top
         str1=str1+'######################################\n'
         str1=str1+'###########             Gate based Verilog             ########\n'
         str1=str1+'######################################\n\n\n\n'
         str1=str1+'######################################\n'
         str1=str1+'###########     File saved as '+ self.textbox1.text()+'.verilog and in 2 other formats   ########\n'
         str1=str1+'######################################\n\n\n'

         self.variables[0]['text']=str1
         self.textbox.setText(self.variables[0]['text'])
      except:
         self.variables[0]['text']='Please Select A CIRC FILE'
         self.textbox.setText(self.variables[0]['text'])


   def ttbased(self):
      try:
         if(self.variables[0]['gogen']==0):
            self.generatevirtualgraph()                 

         fname1=self.textbox1.text()
         pins=self.variables[0]['pins']
         ands_end=self.variables[0]['ands_end']
         or_end=self.variables[0]['or_end']
         nots_end=self.variables[0]['nots_end']
         ops=self.variables[0]['ops']
         wires1=self.variables[0]['wires1']
         connection_and=self.variables[0]['ca']
         connection_or=self.variables[0]['co']
         connection_not=self.variables[0]['cn']
         top=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,2)

         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########         Truth Table based Verilog           ########\n'
         str1=str1+'######################################\n'
         ts='Calculating all the possible combination for the truth table of the verilog file\n'
         for vi in range(200):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         str1=str1+top
         str1=str1+'######################################\n'
         str1=str1+'###########         Truth Table based Verilog           ########\n'
         str1=str1+'######################################\n\n\n\n'

         str1=str1+'######################################\n'
         str1=str1+'###########     File saved as '+ self.textbox1.text()+'.verilog and in 2 other formats   ########\n'
         str1=str1+'######################################\n\n\n'
         self.variables[0]['text']=str1
         self.textbox.setText(self.variables[0]['text'])
      except:
         self.variables[0]['text']='Please Select A CIRC FILE'
         self.textbox.setText(self.variables[0]['text'])

   def abased(self):
      try:
         if(self.variables[0]['gogen']==0):
            self.generatevirtualgraph()                 

         fname1=self.textbox1.text()
         pins=self.variables[0]['pins']
         ands_end=self.variables[0]['ands_end']
         or_end=self.variables[0]['or_end']
         nots_end=self.variables[0]['nots_end']
         ops=self.variables[0]['ops']
         wires1=self.variables[0]['wires1']
         connection_and=self.variables[0]['ca']
         connection_or=self.variables[0]['co']
         connection_not=self.variables[0]['cn']
         top=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,3)

         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########         Assign based Verilog           ########\n'
         str1=str1+'######################################\n'
         ts='Finding the correct order in which the wires should be assigned for verilog files\n'
         for vi in range(200):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.005
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         str1=str1+top
         str1=str1+'######################################\n'
         str1=str1+'###########         Assign based Verilog           ########\n'
         str1=str1+'######################################\n\n\n\n'

         str1=str1+'######################################\n'
         str1=str1+'###########     File saved as '+ self.textbox1.text()+'.verilog and in 2 other formats   ########\n'
         str1=str1+'######################################\n\n\n'
         self.variables[0]['text']=str1
         self.textbox.setText(self.variables[0]['text'])
      except:
         self.variables[0]['text']='Please Select A CIRC FILE'
         self.textbox.setText(self.variables[0]['text'])
   def camake(self):
      try:
         if(self.variables[0]['gogen']==0):
            self.generatevirtualgraph()                 

         fname1=self.textbox1.text()
         pins=self.variables[0]['pins']
         ands_end=self.variables[0]['ands_end']
         or_end=self.variables[0]['or_end']
         nots_end=self.variables[0]['nots_end']
         ops=self.variables[0]['ops']
         wires1=self.variables[0]['wires1']
         connection_and=self.variables[0]['ca']
         connection_or=self.variables[0]['co']
         connection_not=self.variables[0]['cn']

         top1=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,1)
         top2=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,2)
         top3=print_into_file(fname1,ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not,3)
         
         #p1 = Process(target=find_and_gates_parallel, args=())
         #p1.start()
         #top1=ansav['rt']
         #p2 = Process(target=find_and_gates_parallel, args=())
         #p2.start()
         #top1=ansav['rt']
         #p3 = Process(target=find_and_gates_parallel, args=())
         #p3.start()
         #top1=ansav['rt']
         
         str1=''
         str1=str1+'######################################\n'
         str1=str1+'###########         Running parallelly           ########\n'
         str1=str1+'######################################\n'
         ts='Finding the correct order in which the wires should be assigned for verilog files\n'
         for vi in range(200):
            ts=ts+'#'
            self.variables[0]['text']=ts
            self.textbox.setText(self.variables[0]['text'])
            QApplication.processEvents()         
            timesleep=0.002
            divide=1.0
            if(self.ppchb.isChecked()):
               divide=float(self.ppinp.text())
            sleep(timesleep/divide)
         str1=str1+ '\n\n'+top1+ '\n\n'
         str1=str1+ '\n\n'+top2+ '\n\n'
         str1=str1+ '\n\n'+top3+ '\n\n'
         str1=str1+'######################################\n'
         str1=str1+'###########         Running Parallely           ########\n'
         str1=str1+'######################################\n\n\n\n'

         str1=str1+'######################################\n'
         str1=str1+'###########     File saved as '+ self.textbox1.text()+'.verilog and in 2 other formats   ########\n'
         str1=str1+'######################################\n\n\n'
         self.variables[0]['text']=str1
         self.textbox.setText(self.variables[0]['text'])
      except:
         self.variables[0]['text']='Please Select A CIRC FILE'
         self.textbox.setText(self.variables[0]['text'])
   def ttmake(self):
   	call(['python', 'tt.py'])
	
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()