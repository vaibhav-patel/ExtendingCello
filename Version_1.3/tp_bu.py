import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget,QGridLayout,QPushButton,QTextEdit, QFileDialog,QRadioButton,QHBoxLayout
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


      self.btn1 = QPushButton("Load existing circ file")
      self.btn1.clicked.connect(self.loadexisting)
      xlayout.addWidget(self.btn,0,0)
      xlayout.addWidget(self.btn1,0,1)
      self.b1 = QRadioButton("Display all")
      self.b1.setChecked(True)
      self.b1.toggled.connect(lambda:self.btnstate1())
      xlayout.addWidget(self.b1,0,2)
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

      self.textbox = QTextEdit()
      self.textbox.setReadOnly(True)
      self.textbox.setText('')
      self.variables[0]['text']=''
      self.variables[0]['textbox']=1

 
      
      layout.addWidget(self.textbox)
      self.setLayout(layout)
      self.setWindowTitle("Cello GUI")

   def makeanewexec(self):
      call(['java', '-jar', 'logisim.jar'])
   def generatevirtualgraph(self):
      if(True):
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
               
         #print 'connections'
         #print 'connections not'

         #print connection_not
         #print 'connections and'
         #for i in connection_and:
         #  print (i,connection_and[i])

         #print 'connections or'
         #for i in connection_or:
         #  print (i,connection_or[i])
         #print_into_file('output/first_file',ops,pins,nots_end,ands_end,or_end,connection_and,connection_or,connection_not)

#      except:
#         pass

   def show_wires(self):
      try:
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
         pass

   def show_inputs(self):
      try:
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
         pass

   def show_outputs(self):
      try:
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
         pass

   def show_gates(self):
      try:
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
         pass
   def show_and(self):
      try:
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
         pass
   def show_or(self):
      try:
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
         pass
   def show_not(self):
      try:
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
         pass


   def loadexisting(self):
      #fname = QFileDialog.getOpenFileName(self, 'Open file', 
      #   '/home',"CIRC files (*.circ)")
      with open('example_circuits/full.circ') as f:
         lines_global = f.read().splitlines()
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

   
         
   			
def main():
   app = QApplication(sys.argv)
   ex = filedialogdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()