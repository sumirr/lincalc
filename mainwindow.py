import sys,os


from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPlainTextEdit, QWidget, QTreeWidget
#from PySide6.QtGui import QTextCursor,QFocusEvent,QKeyEvent
from PySide6 import QtGui
from PySide6.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel
from PySide6.QtCore import QObject, QEvent
#from PySide6.QtCore import Qt

from sympy import Trace, pretty, symbols,Matrix,randMatrix, init_printing,pprint,Rational
from sympy.matrices.dense import MutableDenseMatrix
from sympy.matrices.common import ShapeError
from vector import Vector

# mathematical symbols
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,lambda_ = symbols('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,lambda')
#sy.init_printing()
init_printing(use_unicode=True)
#init_printing(use_latex=True)
#sy.printing.latex.latex(math_delim='')


#import numpy as np
from numpy import array

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from help import Help

class vectorFilter(QObject):
    
    style = """
        QPlainTextEdit {
            border: 2px solid lightseagreen;
            border-radius: 5px;
            padding: 5px;
        }
    """
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            #print('in focus: ',obj.objectName())
            if obj.objectName() == 'vectorA':
                obj.setStyleSheet(self.style)
                #print('obj.parent',obj.parent())
                #print('obj.parent().findchildren()',obj.parent().findChildren(QPlainTextEdit))
                    
                for child in obj.parent().findChildren(QPlainTextEdit):
                    if child.objectName() != 'vectorA':
                        #print('child not vectorA')
                        child.setStyleSheet('')
                #obj.setObjectName('edtB')
                #obj.setStyleSheet('')
                #self.ui.edtB.setStyleSheet('')
            elif obj.objectName() == 'vectorB':
                obj.setStyleSheet(self.style)

                #if obj.objectName() == 'edtB':
                #obj.setStyleSheet(self.style)
                #print(obj.parent())
                #print(obj.parent().findChildren(QPlainTextEdit))
                    
                for child in obj.parent().findChildren(QPlainTextEdit):
                    if child.objectName() != 'vectorB':
                        child.setStyleSheet('')
                #self.ui.edtA.setStyleSheet('')
        if event.type() == QEvent.FocusOut:
            #print('out focus',obj.objectName())
            #obj.setStyleSheet('')
            pass
        return super().eventFilter(obj,event)

        #def eventFilter(self,obj,event):
        #        if event.type() == QEvent.KeyPress:
        #            keyEvent = event
        #            print('Ate key press',keyEvent.key())
        #            return True
        #        else:
        #            return super().eventFilter(obj,event)

class eventFilter(QObject):
    style = """
        QPlainTextEdit {
            border: 2px solid lightseagreen;
            border-radius: 5px;
            padding: 5px;
        }
    """

    # def __init__(self,ui):
    #     super().__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)

    # widgets = self.findChildren(QPlainTextEdit)
    #     for widget in widgets:
    #         print(widget.objectName())
                
    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            print('in focus: ',obj.objectName())
            if obj.objectName() == 'edtA':
                obj.setStyleSheet(self.style)
                #print(obj.parent())
                #print(obj.parent().findChildren(QPlainTextEdit))
                    
                for child in obj.parent().findChildren(QPlainTextEdit):
                    if child.objectName() != 'edtA':
                        child.setStyleSheet('')
                #obj.setObjectName('edtB')
                #obj.setStyleSheet('')
                #self.ui.edtB.setStyleSheet('')
            elif obj.objectName() == 'edtB':
                obj.setStyleSheet(self.style)

                #if obj.objectName() == 'edtB':
                #obj.setStyleSheet(self.style)
                #print(obj.parent())
                #print(obj.parent().findChildren(QPlainTextEdit))
                    
                for child in obj.parent().findChildren(QPlainTextEdit):
                    if child.objectName() != 'edtB':
                        child.setStyleSheet('')
                #self.ui.edtA.setStyleSheet('')
        if event.type() == QEvent.FocusOut:
            # print('out focus',obj.objectName())
            #obj.setStyleSheet('')
            pass
        return super().eventFilter(obj,event)


class MainWindow(QMainWindow):
    style = """
        QPlainTextEdit {
            border: 2px solid lightseagreen;
            border-radius: 5px;
            padding: 5px;`
        }
    """

    # this links to the help form
    # sets up a instance, and shows the form
    def contents(self):
        self.help_form = Help()
        self.help_form.show()

    # this variable is needed when receiving input from the edtA and edtB
    # to differentiate between matrices of type float, and matrices of type int
    # used by string_to_matrix function
    # set during validate_user_input
    # [todo] not sure if this needed any more, because the has_floats method iterates through the contents of a matrix and checks if there exists a float inside of it.
    # [possibly outdated]

    matrix_type = "int"

    # list to store the transactions done by the user inside of the program.
    input_list = []

    #
    counter = 1

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ev = eventFilter()
        self.ui.edtA.installEventFilter(self.ev)
        self.ui.edtB.installEventFilter(self.ev)

        self.vF = vectorFilter()

        self.ui.vectorA.installEventFilter(self.vF)
        self.ui.vectorB.installEventFilter(self.vF)
        
        self.ui.btnVectorSwap.setIcon(QIcon('swap.png'))
        self.ui.btnSwap.setIcon(QIcon('swap.png'))        #self.ui.btnPretty.setIcon(QIcon('fraction.png'))

        
    # for vectors, multiplication is performed in terms of dot product and cross product 
    #def vector_multiplication(self):
    #    print('vector multiplication starting')
    #    v = Vector()

    #    # check both vectors have equal dimensions
    #    if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
    #        return
    #    else:
    #        vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
    #    try:
    #        multiplication = v.multiplication(vector_a,vector_b)
    #        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
    #        self.ui.edtOutput.insertPlainText('Vector multiplication: \n\n')
    #        self.ui.edtOutput.insertPlainText(pretty(multiplication,wrap_line=False) + '\n\n')
    #        self.ui.lblOutput.setText('')
    #    except Exception as e:
    #        print('e')
    #        self.ui.lblOutput.setText('Err: Could not process vector multiplication')


    
    # swap the vector values
    def swap_vectors(self):
        vector_a = self.ui.vectorA.toPlainText()
        vector_b = self.ui.vectorB.toPlainText()
        self.ui.vectorA.setPlainText(vector_b)
        self.ui.vectorB.setPlainText(vector_a)



    def vector_subtraction(self):
        print('vector subtraction starting')
        v = Vector()

        # check both vectors have equal dimensions
        if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
            return
        else:
            vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
        try:
            subtraction = v.subtraction(vector_a,vector_b)
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Vector subtraction: \n\n')
            self.ui.edtOutput.insertPlainText(pretty(subtraction,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            print('e')
            self.ui.lblOutput.setText('Err: Could not process vector subtraction')


    def vector_addition(self):
        print('vector addition starting')
        v = Vector()

        # check both vectors have equal dimensions
        if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
            return
        else:
            vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
        try:
            addition = v.addition(vector_a,vector_b)
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Vector addition: \n\n')
            self.ui.edtOutput.insertPlainText(pretty(addition,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            print('e')
            self.ui.lblOutput.setText('Err: Could not process vector addition')
    
    def vector_angle_between(self):
        print('vector angle between starting')
        v = Vector()

        # check both vectors have equal dimensions
        if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
            return
        else:
            vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
        try:
            angle_between = v.angle_between(vector_a,vector_b)
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Angle Between A and B: \n\n')
            self.ui.edtOutput.insertPlainText(pretty(angle_between,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            print('e')
            self.ui.lblOutput.setText('Err: Could not process the angle between')

    # calculates the unit vector of a given vector
    def vector_unit_vector(self):
        print('vector unit vector starting')
        v = Vector()
        active_matrix = self.vector_which_active()
        print('active_matrix',active_matrix)
        matrix = v.get_single_vector_input(active_matrix,self.ui.lblOutput)
        print('matrix',matrix)
        unit_vector = v.unit_vector(matrix)

        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText('Unit Vector: \n\n')
        self.ui.edtOutput.insertPlainText(pretty(unit_vector,wrap_line=False) + '\n\n')
        self.ui.lblOutput.setText('')
    

    # multiplies the vector by a scalar multiple
    def vector_multiply_by(self):
        v = Vector()
        active_matrix = self.vector_which_active()
        matrix = v.get_single_vector_input(active_matrix,self.ui.lblOutput)
        try:
            multiply_by = int(self.ui.edtVectorMultiplyBy.text())
            output = matrix * multiply_by
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str('Vector Multiply By: \n\n'))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.lblOutput.setText('Err: ' + str(e))
            return

    def vector_power_to(self):
        #try:
        
        print('starting vector power to')
        v = Vector()
        active_matrix = self.vector_which_active()
        matrix = v.get_single_vector_input(active_matrix,self.ui.lblOutput)
        power_to = int(self.ui.edtVectorPowerTo.text())
        output = matrix.applyfunc(lambda e: e**power_to)
            
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText('Power To: \n\n')
        self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')

        #except Exception as e:
        #    self.ui.lblOutput.setText('Err: Power To: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Power To: ' + str(e) + '\n\n')

    def vector_magnitude(self):
        print('vector magnitude starting')
        v = Vector()
        active_matrix = self.vector_which_active()
        #matrix = v.get_single_vector_input(active_matrix,self.ui.lblOutput)
        matrix = v.get_single_vector_input(active_matrix,self.ui.lblOutput)
        magnitude = matrix.norm()
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText('Magnitude of vector: \n\n')
        self.ui.edtOutput.insertPlainText(pretty(magnitude,wrap_line=False) + '\n\n')
        self.ui.lblOutput.setText('')
        print('matrix',matrix)
       
    # dimensions of both matrices must the same.
    # calculates the vector projection between two matrices
    def projection(self):
        print('projection starting')
        v = Vector()
        # check both vectors have equal dimensions
        if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
            return
        else:
            
            vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
            projection = v.projection(vector_a,vector_b)
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Projection A along B: \n\n')
            self.ui.edtOutput.insertPlainText(pretty(projection,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        

    # 
    def vector_cross_product(self):
        print('vector_cross_product starting')
        v = Vector()

        # check if the vectors are 3x1
        # cross product only defined for 3 element vector
        if v.size_check(self.ui.vectorA,self.ui.vectorB,3,self.ui.lblOutput) == False:
            return
        else:
            vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
            cross_product = vector_a.cross(vector_b)
            print('cross_product',cross_product)
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Cross Product: \n\n')
            self.ui.edtOutput.insertPlainText(pretty(cross_product,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')

    
    def vector_dot_product(self):
        v = Vector()
        if v.size_check(self.ui.vectorA,self.ui.vectorB,None,self.ui.lblOutput) == False:
            #self.ui.lblOutput.setText('Err: Vector sizes do not match')
            return
        vector_a,vector_b = v.get_both_vector_inputs(self.ui.vectorA,self.ui.vectorB,self.ui.lblOutput)
        dot_product = vector_a.dot(vector_b)
        print('dot_product',dot_product)
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText('Dot Product: \n\n')
        self.ui.edtOutput.insertPlainText(pretty(dot_product,wrap_line=False) + '\n\n')
        self.ui.lblOutput.setText('')

    # swap the matrix values
    def swap_matrices(self):
        matrix_a = self.ui.edtA.toPlainText()
        matrix_b = self.ui.edtB.toPlainText()
        self.ui.edtA.setPlainText(matrix_b)
        self.ui.edtB.setPlainText(matrix_a)

    # calculates the difference between both both matrices
    def difference(self):
        matrix_a,matrix_b = self.get_both_matrix_input()

        try:
            difference = matrix_a - matrix_b
            self.add_to_combobox(difference,'Matrix Difference')
            self.ui.lblOutput.setText('')
        except ShapeError:
            # error_box = QMessageBox()
            # error_box.setWindowTitle('Error')
            # error_box.setText('Matrix shapes are not compatible for difference. Matrices must be the same size')
            # error_box.setIcon(QMessageBox.Warning)
            # error_box.exec()
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err:  Matrix shapes are not compatible for difference' +  '\n\n')
            self.ui.lblOutput.setText('Err:  Matrix shapes are not compatible for difference')
            return

        #print(difference)
        #text = self.return_numpy_array(difference)

        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Matrix Difference: \n\n')
        #self.ui.edtOutput.insertPlainText(text + '\n\n')
        self.ui.edtOutput.insertPlainText(pretty(difference,wrap_line=False) + '\n\n')
        #self.ui.edtOutput.insertPlainText(text + '\n\n')

    # calculates the sum of both matrices
    def sum(self):
        matrix_a,matrix_b = self.get_both_matrix_input()

        try:
              sum = matrix_a + matrix_b

              self.add_to_combobox(sum,'Matrix Addition')
              # self.input_list.append(sum)
              # self.ui.cmbA.addItem(str(self.counter) + ' .Sum')
              # self.counter += 1
              # self.ui.cmbA.setCurrentIndex(self.ui.cmbA.count()-1)

        except ShapeError:
            # error_box = QMessageBox()
            # error_box.setWindowTitle('Error')
            # error_box.setText('Matrix shapes are not compatible for sum. Matrices must be the same size')
            # error_box.setIcon(QMessageBox.Warning)
            # error_box.exec()
            self.ui.lblOutput.setText('Err:  Matrix shapes are not compatible for sum')
            return

        print(sum)
        #text = self.return_numpy_array(sum)
        #self.ui.edtOutpuedtOutputt.setAlignment(Qt.AlignRight)
        self.ui.lblOutput.setText('')
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Matrix Addition: \n\n')
        #self.ui.edtOutput.insertPlainText(text + '\n\n')
        self.ui.edtOutput.insertPlainText(pretty(sum,wrap_line=False) + '\n\n')


    def cross_product(self):
        #return Matrix
        matrix_a,matrix_b = self.get_both_matrix_input()

        try:
            cross_product = matrix_a.cross(matrix_b)
            self.add_to_combobox(cross_product,'Multiplication')

            # self.input_list.append(cross_product)
            # self.ui.cmbA.addItem(str(self.counter) + ' .Dot Product')
            # self.counter += 1
            # self.ui.cmbA.setCurrentIndex(self.ui.cmbA.count()-1)

        except ShapeError:
            self.ui.lblOutput.setText('Err:  Matrix shapes are not compatible for cross product')
            # error_box = QMessageBox()
            # error_box.setWindowTitle('Error')
            # error_box.setText('Matrix shapes are not compatible for dot product.')
            # error_box.setIcon(QMessageBox.Warning)
            # error_box.exec()
            return
        
        #print(cross_product)
        #text = self.return_numpy_array(cross_product)
        self.ui.lblOutput.setText('')
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Cross Product: \n\n')
        #self.ui.edtOutput.insertPlainText(text + '\n\n')
        self.ui.edtOutput.insertPlainText(pretty(cross_product,wrap_line=False) + '\n\n')
        
    
    
    # calculates the dot product of both matrices
    def multiplication(self):
        #return Matrix
        matrix_a,matrix_b = self.get_both_matrix_input()

        try:
            product = matrix_a * matrix_b
            self.add_to_combobox(product,'Matrix Multiplication')

            # self.input_list.append(dot_product)
            # self.ui.cmbA.addItem(str(self.counter) + ' .Dot Product')
            # self.counter += 1
            # self.ui.cmbA.setCurrentIndex(self.ui.cmbA.count()-1)

        except ShapeError:
            self.ui.lblOutput.setText('Err:  Matrix shapes are not compatible for multiplication')
            # error_box = QMessageBox()
            # error_box.setWindowTitle('Error')
            # error_box.setText('Matrix shapes are not compatible for dot product.')
            # error_box.setIcon(QMessageBox.Warning)
            # error_box.exec()
            return
        
        #print(dot_product)
        #text = self.return_numpy_array(dot_product)
        self.ui.lblOutput.setText('')
        self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Matrix Multiplication: \n\n')
        #self.ui.edtOutput.insertPlainText(text + '\n\n')
        self.ui.edtOutput.insertPlainText(pretty(product,wrap_line=False) + '\n\n')

    # calculates the dot product of both matrices
    #def dot_product(self):
    #    #return Matrix
    #    matrix_a,matrix_b = self.get_both_matrix_input()

    #    try:
    #        dot_product = matrix_a.dot(matrix_b)
    #        self.add_to_combobox(dot_product,'Dot Product')

    #        # self.input_list.append(dot_product)
    #        # self.ui.cmbA.addItem(str(self.counter) + ' .Dot Product')
    #        # self.counter += 1
    #        # self.ui.cmbA.setCurrentIndex(self.ui.cmbA.count()-1)

    #    except ShapeError:
    #        self.ui.lblOutput.setText('Err:  Matrix shapes are not compatible for dot product')
    #        # error_box = QMessageBox()
    #        # error_box.setWindowTitle('Error')
    #        # error_box.setText('Matrix shapes are not compatible for dot product.')
    #        # error_box.setIcon(QMessageBox.Warning)
    #        # error_box.exec()
    #        return

    #    #print(dot_product)
    #    #text = self.return_numpy_array(dot_product)
    #    self.ui.lblOutput.setText('')
    #    self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
    #    self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Dot Product: \n\n')
    #    #self.ui.edtOutput.insertPlainText(text + '\n\n')
    #    self.ui.edtOutput.insertPlainText(pretty(dot_product,wrap_line=False) + '\n\n')


    # helper function to validate input
    # [todo] remove. currently unused
    def is_matrix_valid(self,matrix):
        for row in matrix:
            for val in row:
                try:
                    float_val = float(val)
                except ValueError:
                    return False
                if not isinstance(float_val, (int, float)):
                    return False
        return True



    # receives a string input that contains fractions.
    # input_str = '''
        # 1/2,5/6,9/18,
        # 4/5,8/5,2/8,
        # 5/9,4/9,4/5
        # '''
    # returns 
        # 0.5,0.8333333333333334,0.5
        # 0.8,1.6,0.25
        # 0.5555555555555556,0.4444444444444444,0.8
    def convert_fractional_string(self,input_str):
        #print('starting fractional convert')
        #print('input',input_str)
        output_str = ''
        for line in input_str.strip().split('\n'):
            #print('line',line)
            for value in line.split(','):
                #print('value',value)
                if '/' in value:
                    numerator, denominator = value.split('/')
                    result = float(numerator) / float(denominator)
                    output_str += str(float(result)) + ','
                else:
                    out_str = value + ','
            output_str = output_str.rstrip(',') + '\n'
        print('output_str',output_str)
        return output_str

    # validates a matrix that is randomly generated, or user inputted
    # checks for all numeric characters
    # checks that rows have equal columns
    # called like this: if self.validate_user_input(edt.toPlainText()):
    def validate_user_input(self,input):
        not_numeric = ""

        # if the input is 1x1 matrix, then there is
        # going to be no commas
        # and the number of rows is going to 1
        for line in input.strip().split('\n'):
            if len(line) == 1:
                rows = 1

        if '/' in input:
            try:
                input = self.convert_fractional_string(input)
            except Exception as e:
                #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                #self.ui.edtOutput.insertPlainText('Err: Fractional Input:'+  '\n\n')
                self.ui.lblOutput.setText('Err:  Fractional Input')

        if ',' in input:  
            is_numeric = True  

            # if there exists a '/' in matrix, then it needs to convert the whole matrix 
            # to floating point.

            # validates if all elements inside input string are numeric
            for line in input.strip().split('\n'):
                for value in line.split(','):
                    value = value.strip().replace('-','')
                    # if ('/') in value:
                    #     value = '1/2'
                    #     numerator,denominator = value.split('/')
                    #     result = float(numerator) / float(denominator)
                    #     value = str(result)
                    try:
                        float_val = float(value)
                        #print('validate_user_input',type(value),'value is',value)
                        if not value.isdigit():
                            #print('i found a float',value,'setting self.matrix_type to float')
                            self.matrix_type = 'float'
                    except Exception as e:
                        is_numeric = False
                        not_numeric = value
                    if not isinstance(float_val, (int, float)):
                        is_numeric = False
                        not_numeric = value

            if is_numeric:
                rows = input.strip().split('\n')

                # validates if all rows have the same number of columns
                num_cols = len(rows[0].split(','))
                if any(len(row.split(',')) != num_cols for row in rows):
                    #print(input)
                    print('validate_col_input: failed column check')
                    #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                    #self.ui.edtOutput.insertPlainText('Error: Inconsistent Columns \n\n')
                    return False;
                return True
            else:
                #print('validate_user_input: failed numeric check')
                #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                #self.ui.edtOutput.insertPlainText('Error: Not Numeric:' + not_numeric +  '\n\n')
                return False
        # if its a one dimensional matrix, there will no
        elif rows == 1:
            print('rows =1')
            is_numeric = True  
            for value in input.strip().split('\n'):
                value = value.strip().replace('-','')
                try:
                    float_val = float(value)
                    #print('validate_user_input',type(value),'value is',value)
                    if not value.isdigit():
                        #print('i found a float',value,'setting self.matrix_type to float')
                        self.matrix_type = 'float'
                except Exception as e:
                        is_numeric = False
                        not_numeric = value
                if not isinstance(float_val, (int, float)):
                        is_numeric = False
                        not_numeric = value

            if is_numeric:
                rows = input.strip().split('\n')
                # validates if all rows have the same number of columns
                num_cols = len(rows[0].split(','))
                if any(len(row.split(',')) != num_cols for row in rows):
                    #print(input)
                    #print('validate_col_input: failed column check')
                    #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                    #self.ui.edtOutput.insertPlainText('Error: Inconsistent Columns \n\n')
                    return False;
                return True
            else:
                #print('validate_user_input: failed numeric check')
                #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                #self.ui.edtOutput.insertPlainText('Error: Not Numeric:' + not_numeric +  '\n\n')
                return False
        else:
            #print('hi not cols=1 or ,')
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Critical: Not Numeric:' + not_numeric +  '\n\n')
            return False

        # except Exception as e:
        #     self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
        #     #self.ui.edtOutput.insertPlainText('Err:' + str(e) + '\n\n')  
        #     return False

    # converts a user inputted matrix
    # into sympy matrix
    # self.matrix_type is set during a previous function call to 
    # def validate_user_input(self,input):
    def string_to_matrix(self,matrix_str):
        
        # self.matrix_type = "int"
        # for row in matrix_str.strip().split('\n'):
        #     for value in row.split(',').strip():
        #         if not value.isdigit():
        #             self.matrix_type = 'float'
        #             print('string_to_matrix: setting to float because value:', value)

        if '/' in matrix_str:
            matrix_str = self.convert_fractional_string(matrix_str)        
        
        has_float =  False
        for line in matrix_str.strip().split('\n'):
            for value in matrix_str.split(','):
                value = value.strip().replace('-','')
                num_decimals = value.count('.')
                num_digits = sum(char.isdigit() for char in value)
                if num_decimals == 1 and num_digits > 0:
                    has_float = True

        #if self.matrix_type == "int":
        if has_float == False:
            matrix_list = [list(map(int, row.split(','))) for row in matrix_str.strip().split('\n')]
        else: 
            matrix_list = [list(map(float, row.split(','))) for row in matrix_str.strip().split('\n')]
            
        # convert the list into a SymPy matrix
        matrix_sympy = Matrix(matrix_list)
        #print('matrix_sympy',matrix_sympy)
        # return the SymPy matrix
        return matrix_sympy


    def multiply_by(self):
        try:
            active_matrix = self.which_active()
            matrix = self.get_single_matrix_input(active_matrix)
            multiply_value = int(self.ui.edtMultiply.text())

            output = matrix * multiply_value
            self.add_to_combobox(output,'Multiply By')
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Multiply By: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.lblOutput.setText('Err: Multiply By: ' + str(e))
            #print('could not process matrix for Inverse:',e)

    # take a matrix, and raises it to a power
    def power_of(self):
        try:
            active_matrix = self.which_active()
            matrix = self.get_single_matrix_input(active_matrix)
            power_to = int(self.ui.edtPower.text())

            output = matrix.applyfunc(lambda e: e**power_to)
            self.add_to_combobox(output,'Power To')
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Power To: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Power To: ' + str(e) + '\n\n')
            #print('could not process matrix for Inverse:',e)
            self.ui.lblOutput.setText('Err: Power To: ' + str(e))

    def echelon(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:', matrix)

            output = matrix.echelon_form()
            self.add_to_combobox(output,'Echelon Form')
            #print('output',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Echelon Form: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            #print('pretty output cofactor:',pretty(output))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')    
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Echelon Form \n\n')
            self.ui.lblOutput.setText('Err: Echelon Form: ' + str(e))
            #print('could not process matrix for conjugate:',e)

    def conjugate(self):
        
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:', matrix)

            output = matrix.conjugate()
            self.add_to_combobox(output,'Conjugate')
            #print('output',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Conjugate : \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            #print('pretty output cofactor:',pretty(output))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')    
            self.ui.lblOutput.setText('')
        except Exception as e:
            # self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.lblOutput.setText('Err: Conjugate: ' + str(e))
            #self.ui.edtOutput.insertPlainText('Err: Conjugate \n\n')


    # calculates adjugate of a matrix
    # adjugate = adjugate same term. apparently not according to sympy
    # A.adjugate() does not yield the same result as A.adjugate()
    def adjugate(self):
        
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:', matrix)

            output = matrix.adjugate()
            self.add_to_combobox(output,'Adjugate')
            #print('output',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Adjugate : \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            #print('pretty output cofactor:',pretty(output))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')    
            self.ui.lblOutput.setText('')
        except Exception as e: 
            self.ui.lblOutput.setText('Err: Adjugate: ' + str(e))
            print('could not process matrix for Adjugate:',e)
    #print('could not process matrix for conjugate:',e)

    # calculates adjoint of a matrix
    # adjugate = adjoint same term. apparently not according to sympy
    # A.adjoint() does not yield the same result as A.adjugate()
    def adjoint(self):
        
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:', matrix)

            output = matrix.adjoint()
            self.add_to_combobox(output,'Adjoint')
            #print('output',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Adjoint : \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            #print('pretty output cofactor:',pretty(output))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')    
            self.ui.lblOutput.setText('')
        except Exception as e: 
            self.ui.lblOutput.setText('Err: Adjoint: ' + str(e))
            print('could not process matrix for Adjoint:',e)


    # inverse method has to make use sympys pretty method.
    # due to the fractions
    def inverse(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:',matrix)
            output = matrix.inv()
            output_formatted = output.evalf(2)
            self.matrix_type = "float"

            self.add_to_combobox(output_formatted,'Inverse')

            print('inverse:',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Inverse: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.lblOutput.setText('Err: Inverse: ' + str(e))
            #self.ui.edtOutput.insertPlainText('Err: Inverse: ' + str(e) + '\n\n')
            #print('could not process matrix for Inverse:',e)

    # calculates the jordan_form
    def jordan_form(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:',matrix)
            output = matrix.jordan_form(calc_transform=False)
            self.add_to_combobox(output,'Jordan Form')
            #print('output:',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Jordan Form: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.lblOutput.setText('Err: Jordan Form: ' + str(e))
            #self.ui.edtOutput.insertPlainText('Err: Jordan Form \n\n')
            #print('could not process matrix for Jordan Form:',e)

    # calculates the reduced row echelon form of a given matrix
    def rref(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix:',matrix)
            output = matrix.rref(pivots=False)
            self.add_to_combobox(output,'Reduced Row Echelon')
            #print('output:',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Reduced Row Echelon: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: RREF \n\n')
            self.ui.lblOutput.setText('Err: RREF: ' + str(e))
            #print('could not process matrix for RREF:',e)


    def rank(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            output = matrix.rank()
            #print('output rank', output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Rank: \n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Rank \n\n')
            self.ui.lblOutput.setText('Err: Rank: ' + str(e))
            print('could not process matrix for Rank:',e)

    def transpose(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            output = matrix.T
            self.add_to_combobox(output,'Transpose')
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'Transpose: \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.lblOutput.setText('Err: Transpose: ' + str(e))
            print('could not process matrix for Transpose:',e)

    def permanent(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.per()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Permanent: \n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Permanent: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Err: Permanent \n\n')
            print('could not process matrix for Trace:',e)

    def trace(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = Trace(matrix).simplify()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Trace: \n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Trace: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Trace \n\n')
            print('could not process matrix for Trace:',e)


    # calculates the eigen_values of a given matrix
    def eigen_values(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.eigenvals()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Eigen Values: \n')
            #self.ui.edtOutput.insertPlainText(str(output) + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Eigen Values: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Eigen Values \n\n')
            print('could not process matrix for Eigen Values:',e)

    

    # calculates is a matrix is skew-symmetric
    # A skew-symmetric matrix is a square matrix whose transpose is equal to its negative
    # that is A^T = -A

    def skew_symmetric(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            #output = matrix.is_symmetric()
            if matrix.transpose() == matrix*(-1):
                output = True
            else:
                output = False

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Skew-Symmetric: \n')
            self.ui.edtOutput.insertPlainText(pretty(output) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Skew-Symmetric: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Skew-Symmetric \n\n')
            print('could not process matrix for Skew-Symmetric:',e)



     # calculates if a matrix is symmetric
    def hermitian(self):
        #print('determinant')
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.is_hermitian

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Hermitian: \n')
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Hermitian: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Hermitian \n\n')
            print('could not process matrix for Hermitian:',e)

    # calculates if a matrix is symmetric
    def symmetric(self):
        #print('determinant')
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.is_symmetric()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Symmetric: \n')
            self.ui.edtOutput.insertPlainText(pretty(output) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Symmetric: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Symmetric \n\n')
            print('could not process matrix for Symmetric:',e)

    # calculates the determinant of a given matrix
    def norm(self):
        #print('determinant')
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.norm()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Norm: \n')
            self.ui.edtOutput.insertPlainText(pretty(output) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Norm: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Norm \n\n')
            print('could not process matrix for Norm:',e)

    # calculates the determinant of a given matrix
    def determinant(self):
        #print('determinant')
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            #print('matrix for det: ',matrix)
            output = matrix.det()

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Determinant: \n')
            self.ui.edtOutput.insertPlainText(pretty(output) + '\n\n')
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: Determinant: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Determinant \n\n')
            print('could not process matrix for determinant:',e)

    '''
    1. There could input in both a and b
        -> then default to a
    2. b could be empty
        -> default to a
    4. a could be empty, b contain data

    3. a and b could be empty
        -> request input

    '''
    # might receive a edtA, or edtB
    # should just have the job of cofactoring
    def cofactor_matrix(self):
        
        try:
            active_matrix = self.which_active()
            print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here

            print('matrix:', matrix)

            output = matrix.cofactorMatrix()
            self.add_to_combobox(output,'CoFactor')
            print('output',output)
            #formatted_numpy_array = self.return_numpy_array(output)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText(str(self.counter-1)+'. ' + 'CoFactor : \n\n')
            #self.ui.edtOutput.insertPlainText(formatted_numpy_array + '\n\n')
            #print('pretty output cofactor:',pretty(output))
            self.ui.edtOutput.insertPlainText(pretty(output,wrap_line=False) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')  
            self.ui.lblOutput.setText('')
        except Exception as e:
            self.ui.lblOutput.setText('Err: CoFactor: ' + str(e))
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Cofactor \n\n')
            print('could not process matrix for cofactor:',e)


    # takes a float number like 0.33 and converts it to a fraction
    # like 1/3
    # [todo] rename this function to fraction
    # [todo] currently unused, as btnPretty was deleted
    # the issue was the rounding of floating point numbers to 2 decimal places
    # and then converting back into fractions yielded different results
    def pretty(self):
        try:
            active_matrix = self.which_active()
            #print('active_matrix',active_matrix)
            matrix = self.get_single_matrix_input(active_matrix) # validation occurs here
            print('before pretty matrix',matrix)           
            
            # convert to rational numbers
            rational_m = matrix.applyfunc(lambda x: Rational(x).limit_denominator())

            print('pretty rantional_m',rational_m)

            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Fractional Output:' + '\n\n')
            self.ui.edtOutput.insertPlainText(pretty(rational_m) + '\n\n')
            #self.ui.edtOutput.insertPlainText(output.to_csv() + '\n\n')
        except Exception as e:
            self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            self.ui.edtOutput.insertPlainText('Err: Fraction \n\n')
            print('could not process matrix for Fraction:',e)

    # determines which Vector Input is active
    def vector_which_active(self):
        print('vector_which_active starting')
        if (self.ui.vectorA.toPlainText() == "") and (self.ui.vectorB.toPlainText() == ""):
            self.ui.lblOutput.setText('Err: No input given')
            return
        if self.ui.vectorA.styleSheet() != "":
            return self.ui.vectorA
        elif self.ui.vectorB.styleSheet() != "":
            return self.ui.vectorB

    # determine which QPlainTextEdit is active
    # for matrix
    def which_active(self):
        #print('inside which_active')
        if self.ui.edtA.styleSheet() != "":
            #print('a is active')
            return self.ui.edtA
        elif self.ui.edtB.styleSheet() != "":
            #print('b is active')
            return self.ui.edtB
        #print('which_active: exiting')

    # get the value from both matrices
    # dosnt allow empty values
    def get_both_matrix_input(self):

        # msg_box = QMessageBox()
        # msg_box.setIcon(QMessageBox.Warning)
        # msg_box.setWindowTitle("Warning")
        # # add a button to the message box
        # msg_box.addButton(QMessageBox.Ok)

        if self.ui.edtA.toPlainText().strip() == "":
            #print('hi')
            #msg_box.setText("No values entered in Matrix A")
            # set the detailed text (optional)
            #msg_box.setDetailedText('''Please enter some values in Matrix A:
            # 1,2,3
            # 4,5,6
            # 7,8,9
            #     ''')
            #button_clicked = msg_box.exec_()
            #if button_clicked == QMessageBox.Ok:
            #    self.ui.edtA.setFocus()
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Matrix A is empty \n\n')
            self.ui.lblOutput.setText('Err: Matrix A is empty')
            #print('could not process matrix for Fraction:',e)
        elif self.ui.edtB.toPlainText().strip() == "":
            # msg_box.setText("No values entered in Matrix B")
            # # set the detailed text (optional)
            # msg_box.setDetailedText("Please enter some values in Matrix B")
            # button_clicked = msg_box.exec_()
            # if button_clicked == QMessageBox.Ok:
            #     self.ui.edtB.setFocus()
            #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
            #self.ui.edtOutput.insertPlainText('Err: Matrix B is empty \n\n')
            self.ui.lblOutput.setText('Err: Matrix B is empty')
        else:
            try:
                self.validate_user_input(self.ui.edtA.toPlainText())
                matrix_a = self.string_to_matrix(self.ui.edtA.toPlainText())
                try:
                    self.validate_user_input(self.ui.edtB.toPlainText())
                    matrix_b = self.string_to_matrix(self.ui.edtB.toPlainText())
                    return matrix_a,matrix_b
                except Exception as e:
                    #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                    #self.ui.edtOutput.insertPlainText('Err: Incorrect Input Matrix B \n\n')
                    self.ui.lblOutput.setText('Err: Incorrect Input Matrix B')
                    #sys.exit()
                    print('could not process matrix for input B:',e) 
            except Exception as e:
                #self.ui.edtOutput.moveCursor(QtGui.QTextCursor.Start)
                #self.ui.edtOutput.insertPlainText('Err: Incorrect Input Matrix A \n\n')
                self.ui.lblOutput.setText('Err: Incorrect Input Matrix A')
                #sys.exit()
                print('could not process matrix for input A:',e) 

    # gets the value/user input from EITHER edtA/edB (QPlainTextEdits)
    def get_single_matrix_input(self,edt):
        #print('start single get')
        #print(edt)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.addButton(QMessageBox.Ok)

        if edt.toPlainText().strip() == "":
            self.ui.lblOutput.setText('Err: No values entered')
            self.ui.edtA.setFocus()
            #print('hi')
            #msg_box.setText("No values entered into Matrix")
            # set the detailed text (optional)
            #msg_box.setDetailedText('''Please enter some value:
            #1,2,3
            #4,5,6
            #7,8,9
            #    ''')
            #button_clicked = msg_box.exec_()
            #if button_clicked == QMessageBox.Ok:
            #    #self.ui.edtA.setFocus()
            #    active_matrix = self.which_active()
            #    active_matrix.setFocus()
        else:
            if self.validate_user_input(edt.toPlainText()):
                #print('validate success')
                matrix_a = self.string_to_matrix(edt.toPlainText())
                #print('string_to_matrix success')
                return matrix_a
            else:
                self.ui.lblOutput.setText('Err: Unable to get matrix in correct format')
                raise ValueError('unable to get matrix in correct format')


    # set the stylesheet for a a QPlainTextEdit
    def set_stylesheet(self,edt):
        edt.setStyleSheet(self.style)

    # inserts a sympy mutable dense matrix into  to the combobox cmbA
    # this gets called through a signal emitted from the button click
    # on the form for Insert Into Button under Matrix A
    def insertA(self):
        #print('insert into clicked')
        if self.ui.cmbA.count() != 0:
            selected_index = self.ui.cmbA.currentIndex()
            print('current_index_is: ',str(selected_index))
            self.ui.edtA.clear()

            #type_data = my_list[selected_index]
            item = self.input_list[selected_index]            

            if type(item) == MutableDenseMatrix:
                #print('i found a MutableDenseMatrix')

                #print('selected index',selected_index)
                #print('inverse item',item)
                output = self.return_numpy_array(item)

            self.ui.edtA.insertPlainText(output)
            print('type:',type(item))

    
    # inserts a sympy mutable dense matrix into  to the combobox cmbB
    def insertB(self):
        #print('insert into clicked')
        if self.ui.cmbB.count() != 0:
            selected_index = self.ui.cmbB.currentIndex()
            print('current_index_is: ',str(selected_index))
            self.ui.edtB.clear()

            #type_data = my_list[selected_index]
            item = self.input_list[selected_index]
            if type(item) == MutableDenseMatrix:
                #print('i found a MutableDenseMatrix')
                output = self.return_numpy_array(item)

            self.ui.edtB.insertPlainText(output)
            print('type:',type(item))


    # generate random matrice for first QPlainTextEdit A
    def random_matrix(self):
        self.matrix_type = 'int'
        randomMatrixSize = self.ui.lblSliderA.text()
        print('randomMatrixSize',randomMatrixSize)
        #a = randMatrix(int(randomMatrixSize),min=0,max=5,percent=80)
        a = randMatrix(int(randomMatrixSize),min=0,max=5)
        formatted_numpy_array = self.return_numpy_array(a)
        self.ui.edtA.setPlainText(pretty(formatted_numpy_array))
        
        self.set_stylesheet(self.ui.edtA)
        self.ui.edtB.setStyleSheet('')


    # generate random matrice for second QPlainTextEdit B
    def random_matrixb(self):
        self.matrix_type = 'int'
        randomMatrixSize = self.ui.lblSliderB.text()
        #print('randomMatrixSize',randomMatrixSize)
        #print('randomMatrixSize(int)',int(randomMatrixSize))
        #b = randMatrix(int(randomMatrixSize),min=0,max=5,percent=80)
        #print('b',b)
        b = randMatrix(int(randomMatrixSize),min=0,max=5)
        formatted_numpy_array = self.return_numpy_array(b)
        self.ui.edtB.setPlainText(pretty(formatted_numpy_array))
        self.set_stylesheet(self.ui.edtB)
        self.ui.edtA.setStyleSheet('')


    # takes a sympy matrix and adds it to input_list
    # so that it can be retrieved later

    def add_to_combobox(self,sympyMatrix,operation):
        #print('add_to_combobox',sympyMatrix)
        self.input_list.append(sympyMatrix)
        self.ui.cmbA.addItem(str(self.counter) + '. ' + operation)
        self.ui.cmbB.addItem(str(self.counter) + '. ' + operation)
        
        self.counter += 1

        self.ui.cmbA.setCurrentIndex(self.ui.cmbA.count()-1)
        self.ui.cmbB.setCurrentIndex(self.ui.cmbB.count()-1)


    # receives a sympy matrix
    # iterates through each item, converting it to a string
    # and counts the number of decimal points and number of digits in the string
    def has_floats(self,matrix):
        has_float = False
        for elem in matrix:
            #print('has_floats:elem',str(elem))
            item = str(elem)
            num_decimals = item.count('.')
            num_digits = sum(char.isdigit() for char in item)
            if num_decimals == 1 and num_digits > 0:
                has_float = True
        return has_float

    # function convert a sympy matrix into numpy for textedit format and display
    # used for displaying the matrices in the QPlainTextEdits
    # used by random functions to generate matrices for edtA and edtB
    def return_numpy_array(self,sympyMatrix):
        #arr = np.array(sympyMatrix).astype(np.float64)
        print('return_numpy_array,sympyMatrix',str(sympyMatrix))
        has_float = self.has_floats(sympyMatrix)
        print('return_numpy_array,has_floats',has_float)
        

        if has_float:
            arr = array(sympyMatrix).astype(float)
            
            # Calculate the maximum length of each column
            max_lengths = [max([len('{:0.0f}'.format(item)) for item in col]) for col in zip(*arr)]
            
            x = '\n'.join([', '.join(['{:0.2f}'.format(item).ljust(length) for item, length in zip(row, max_lengths)]) for row in arr])
        else:
            arr = array(sympyMatrix).astype(int)

            # Calculate the maximum length of each column
            max_lengths = [max([len('{:0.0f}'.format(item)) for item in col]) for col in zip(*arr)]

            x = '\n'.join([', '.join(['{:0.0f}'.format(item).ljust(length) for item, length in zip(row, max_lengths)]) for row in arr])
        print('arr\n',arr)

        

        # if has_floats:
        #     print('matrix_type',self.matrix_type)
        # # Join the array, left-aligning each value in a column with a fixed width
        #     x = '\n'.join([', '.join(['{:0.0f}'.format(item).ljust(length) for item, length in zip(row, max_lengths)]) for row in arr])
        # else:
        #     x = '\n'.join([', '.join(['{:0.2f}'.format(item).ljust(length) for item, length in zip(row, max_lengths)]) for row in arr])
        return x

    # close the application
    def exit_app(self,checked):
        QApplication.quit()

    # bring up a QMessageBox detailing the about of the application.
    def about(self):
        
         # Create a custom QMessageBox with the same label as the central widget
        message_box = QMessageBox(self)
        message_box.setWindowTitle("About the Matrix Calculator App")
        message_box.setText("Welcome to the Matrix Calculator App!<br><br>"
                     "This app allows you to perform various operations on matrices.<br><br>"
                     "We hope that you enjoy using this application, and would love to hear from you.<br><br>"
                            "Please<a href='mailto: matrix@sura.co.za'>Contact Us</a> with your feedback.<br><br>"
                     "Happy calculating!")
        message_box.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.setWindowTitle('Linear Algebra Calculator') 

    # qss_file = os.path.abspath(os.path.join(os.getcwd(),"dark_purple.css"))
    # print('qss_file',qss_file)
    # with open(qss_file,"r") as f:
    #     style = f.read()

    # widget.setStyleSheet(style)

    widget.show()
    sys.exit(app.exec())
