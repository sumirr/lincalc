#from PySide6 import QtGui
from sympy import Matrix
from math import acos,degrees

class Vector():

    def __init__(self):
        super().__init__()
   
    # receives two sympy matrix as parameters
    # returns the angle between the two vectors
    # returns a fstring with the angle in radians and degrees
    def angle_between(self,u,v):
        angle = ((u.dot(v)/(u.norm()*v.norm())))
        #print('angle: ',angle)
        deg_answer = degrees(acos(angle))
        rad_answer = acos(angle)

        formatted_deg = "{:.2f}".format(deg_answer)
        formatted_rad = "{:.2f}".format(rad_answer)

        answer = f"cos^-1({angle}) = {formatted_rad} radians = {formatted_deg} degrees"
        return answer
   

    # calculates the multiplication of two vectors
    #def multiplication (self,u,n):
    #   return u * n
    
    # calculates the subtraction of two vectors
    def subtraction(self,u,n):
       return u - n

    # calculates the addition of two vectors
    def addition(self,u,n):
        return u + n

    # calculates the vector projection between two matrices
    def projection(self,u, n):
        return (u.dot(n)/n.norm()**2)*n 

    # calculate the unit vector of a vector
    def unit_vector(self,vector):
        return vector * (1/vector.norm())
    
    # returns a sympy matrix after being passed a editBox
    def get_single_vector_input(self,edt,lblOutput):
        if edt.toPlainText().strip() == "":
            lblOutput.setText('Err: Vector is empty')
            edt.setFocus()
        else:
            try:
                if self.validate_user_input(edt.toPlainText()):
                    vector = self.string_to_matrix(edt.toPlainText())
                    #print('\t self_string_to_matrix: ',str(vector))
                    return vector
                else:
                    edt.setFocus()
                    lblOutput.setText('Err: Incorrect Input')
            except Exception as e:
                lblOutput.setText('Err: Incorrect Input')
                edt.setFocus()

    def get_both_vector_inputs(self, edtA, edtB, lblOutput):
        if edtA.toPlainText().strip() == "":
            lblOutput.setText('Err: Vector A is empty')
            edtA.setFocus()
        elif edtB.toPlainText().strip() == "":
            lblOutput.setText('Err: Vector B is empty')
            edtB.setFocus()
        else:
            try:
                print('Vector get_both_vector_inputs: starting')
                if self.validate_user_input(edtA.toPlainText()):
                    print('Vector get_both_vector_inputs: validate_user_input A passed')
                    vector_a = self.string_to_matrix(edtA.toPlainText())
                    print('vector_a: ',str(vector_a))
                    try:
                        print('trying to validate vector B')
                        if self.validate_user_input(edtB.toPlainText()):
                            vector_b = self.string_to_matrix(edtB.toPlainText())
                            print('Vector get_both_vector_inputs: validate_user_input B passed')
                            print('vector_b',vector_b)
                            return vector_a,vector_b
                        else:
                            edtB.setFocus()
                            lblOutput.setText('Err: Incorrect Input Vector B')
                    except Exception as e:
                        lblOutput.setText('Err: Incorrect Input Vector B')
                        edtB.setFocus()
                else:
                    edtA.setFocus()
                    lblOutput.setText('Err: Incorrect Input Vector A')
            except Exception as e:
                edtA.setFocus()
                lblOutput.setText('Err: Incorrect Input Vector A')
   
    # check if the elements in edtA and edtB have the same number of dimensions
    def size_check(self,edtA,edtB,size=None,lblOutput=None):
        print('size_check: starting')
        # check if the vectors are the same size
        num_elements_A = len(edtA.toPlainText().split(','))
        num_elements_B = len(edtB.toPlainText().split(','))
        
        if size != None:
            if num_elements_A == size and num_elements_B == size:
                return True
            else:
                lblOutput.setText('Err: Vectors must contain ' + str(size) + ' elements')
                return 
        elif num_elements_A == num_elements_B:
            print('size_check: passed')
            return True
        else:
            lblOutput.setText('Err: Vector sizes do not match')
            print('size_check: failed')
            return False

    # performs some standard validation across all vector operations
    # 1. If the vector is comma seperated
    # 2. If the vector is a single row
    # 3. If the vector is numeric 
    def validate_user_input(self,input):
        print('validate_user_input: starting')
        input = input.strip()
        
        try:
            if '/' in input:
                input = self.convert_fractional_string(input)
                print('\t fractional vector:',input)
        except Exception as e:
            print('Err: could not process fractional input')
            return False

        if ',' in input:
            is_numeric = True
            if input.count('\n') == 0:
                print('one row check pass')
                try:
                    for value in input.split(','):
                        value = value.strip().replace('-','')
                        try:
                            float_val = float(value)
                        except Exception as e:
                            is_numeric = False
                            not_numeric = str(value)
                            print('Err: encountered non numeric: ',not_numeric)
                except Exception as e:
                    print('error in numeric validation')
                    return False
            else:
                print('error in row check')
                return False

           
            if is_numeric:
                print('validate_user_input: is_numeric passed')
                return True
            else:
                print('validate_user_input: is_numeric failed')
                return False
        else:
            print('not comma seperated')
    
    # converts a string of fractions to a string of floats
    def convert_fractional_string(self,input):
        print('convert_fractional_string: starting')
        print('convert_fractional_string: input: ',input)
        output_str = ''
        
        #print('err',input.strip().split(',')[s-1])

        for value in input.strip().split(','):
            print('convert_fractional_string: value: ',value)
            if '/' in value:
                numerator,denominator = value.split('/')
                result = float(numerator) / float(denominator)
                
                if value == input.strip().split(',')[-1]:
                    output_str += str(float(result))
                else:
                    output_str += str(float(result)) + ','
            else:
                # if value is the last element in the list
                if value == input.strip().split(',')[-1]:
                    output_str += value
                else:
                    output_str += value + ','
            print('\t\tconvert_fractional_string: output_str: ',output_str)

        print('convert_fractional_string: output_str: ',output_str)
        return output_str
    
    # converts a string of numbers to a sympy matrix
    def string_to_matrix(self,matrix):
        print('string to matrix starting')
        print('string_to_matrix: matrix: ',matrix)
        if '/' in matrix:
            matrix = self.convert_fractional_string(matrix)
        has_float = False
        for line in matrix.strip().split('\n'):
            for value in matrix.split(','):
                value = value.strip().replace('-','')
                num_decimals = value.count('.')
                num_digits = sum(char.isdigit() for char in value)
                if num_decimals == 1 and num_digits > 0:
                    has_float = True

        if has_float == False:
            matrix_list = [list(map(int, row.split(','))) for row in matrix.strip().split('\n')]
        else:
            matrix_list = [list(map(float, row.split(','))) for row in matrix.strip().split('\n')]

        matrix_sympy = Matrix(matrix_list)
        return matrix_sympy

