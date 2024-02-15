# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QWidget
from help_ui import Ui_Form


class Help(QWidget):
    style_sheet = """
    QTreeView {
        background-color: #222;
        color: #fff;
        selection-background-color: #444;
        selection-color: #fff;
        border: none;
    }

    QPlainTextEdit {
        background-color: #222;
        color: #fff;
        border: none;
    }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.tree_view = self.ui.treeView

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Contents'])

        parent_item = model.invisibleRootItem()

        # self.tree_view.setStyleSheet(style_sheet)
        # self.edtHelp.setStyleSheet(style_sheet)

        # Add top-level items
        item1 = QStandardItem("How to use")
        item2 = QStandardItem("Matrix Definitions")
        item3 = QStandardItem("Fractions and Float Matrices")
        item4 = QStandardItem("Vector Definitions")
        # parent_item.insertRow([item1, item2, item3]T)
        parent_item.insertRow(0, [item1])
        parent_item.insertRow(1, [item2])
        parent_item.insertRow(2, [item3])
        parent_item.insertRow(3, [item4])

        # Add child items to Item 1
        # child_item1 = QStandardItem("Definitions")
        # child_item2 = QStandardItem("Fractional ")
        # #item1.insertRow(0, [child_item1])
        # item2.insertRow(0, [child_item1])

        self.tree_view.setModel(model)

        # self.layout = QHBoxLayout()
        # self.setFixedSize(400,300)

        self.ui.treeView.clicked.connect(self.on_treeView_clicked)

    def on_treeView_clicked(self, index):
        print('one_treeView_clicked => treeview clicked')
        item = self.ui.treeView.model().itemFromIndex(index)
        text = item.text()
        print('text which was clicked',text)
        if text == "Matrix Definitions":
            text = '''• Addition and subtraction: The sum or difference of two matrices of the same dimensions is obtained by adding or subtracting the corresponding entries.

            ⎡3  1⎤      ⎡1  4⎤     ⎡4  5⎤
            ⎣4  2⎦  +   ⎣2  1⎦  =  ⎣6  3⎦ \n\n 
• Scalar multiplication: Multiplying a matrix by a scalar multiplies each entry of the matrix by the scalar.
               ⎡3  1⎤       ⎡9   3⎤       
           3 x ⎣4  2⎦   =   ⎣12  6⎦        

• Matrix multiplication: The product of two matrices A and B is obtained by multiplying the rows of A by the columns of B.
            ⎡3  1⎤      ⎡1  4⎤     ⎡5  13⎤
            ⎣4  2⎦  x   ⎣2  1⎦  =  ⎣8  18⎦ 

• Transpose: The transpose of a matrix A is obtained by interchanging its rows and columns.
                 ⎡3  1⎤                 ⎡3  4⎤    
           A =   ⎣4  2⎦  A.Transpose =  ⎣1  2⎦

• Determinant: The determinant of a square matrix A is a scalar value that can be computed using various methods and provides important information about the matrix, such as whether it is invertible or not.
            
                 ⎡3  1⎤             
           A =   ⎣4  2⎦  det(A) =  2

• Inverse: The inverse of a square matrix A is another square matrix A^-1, such that AA^-1 = A^-1A = I, where I is the identity matrix.

                 ⎡3  1⎤              ⎡1  -1/2⎤    
           A =   ⎣4  2⎦  A.Inverse = ⎣-2  3/2⎦

• Trace: The trace of a square matrix A is the sum of its diagonal entries.
            
                 ⎡3  1⎤               
           A =   ⎣4  2⎦  A.Trace = 5

• Eigenvalues and eigenvectors: Eigenvalues and eigenvectors provide important information about a matrix, such as how it scales certain vectors.

                 ⎡3  1⎤    ⎧5   √17     √17   5   ⎫
           A =   ⎣4  2⎦    ⎨─ - ───: 1, ─── + ─: 1⎬
                           ⎩2    2       2    2   ⎭

• Rank: The rank of a matrix is the dimension of the subspace spanned by its columns or rows.
            
                 ⎡3  1⎤               
           A =   ⎣4  2⎦  A.Rank = 2

• Adjoint: Returns the conjugate transpose of a matrix. The adjoint is the transpose of the conjugate of a matrix. The conjugate of a matrix is obtained by conjugating each element of the matrix. The conjugate of a complex number is the number with the same real part and imaginary part equal in magnitude but opposite in sign. 
        
                 ⎡3  1⎤               ⎡3  4⎤
           A =   ⎣4  2⎦  A.Adjoint =  ⎣1  2⎦


• Adjugate: Returns the adjugate of a matrix. The adjugate of a matrix is also known as the classical adjoint, and it is defined as the transpose of the cofactor matrix of a matrix. The cofactor of an element of a square matrix is the signed determinant of the submatrix obtained by deleting the row and column containing that element.

        A =  ⎡3  1⎤               ⎡2  -1⎤
             ⎣4  2⎦  A.Adjugate = ⎣-4  3⎦


• Cofactor: The cofactor of an element of a square matrix is the signed determinant of the submatrix obtained by deleting the row and column containing that element.

                 ⎡3  1⎤               ⎡2  -4⎤
           A =   ⎣4  2⎦  A.CoFactor = ⎣-1  3⎦
            '''
        elif text == "How to use":
            text = ''' 

+---------+
| Matrix  |
+---------+

1. User Input
The program works by accepting user input in form of comma separated values. For example to input a 3 x 3 matrix:
            1,2,3
            4,5,6
            7,8,9
            
2. Random Slider
The random slider generates square matrices with values in the range of 0 to 5. The minimum random matrix generated is 1 x 1 and the maximum generated random matrix is 10 x 10

            3, 0, 3
            2, 3, 1
            2, 2, 0

+----------------+
| Vector         |
+----------------+

The program supports insertion of row vectors. A row vector is a vector that has only one row and multiple columns. Each element in the row corresponds to a component of the vector. For example, a row vector with three columns could represent a 3-dimensional vector with x, y, and z components.

A row vector can be inserted in the following way:
    1,2,3

Support for floating-point numbers is also available. For example, the following row vector represents a 3-dimensional vector with x, y, and z components.
    1.2,2.3,3.4



            '''    
        elif text == "Fractions and Float Matrices":
            text = ''' Matrices with fractions are supported. For example, you can enter in a matrix with fractions like this:
            
            1/2,5/6,9/18
            4/5,8/5,2/8
            5/9,4/9,4/5

If you use the Power To function and raise this matrix to the power of 1, it will be visible in the output window.

            2. Power To: 

        ⎡       0.5         0.833333333333333  0.5 ⎤
        ⎢       0.8                1.6         0.25⎥
        ⎣0.555555555555556  0.444444444444444  0.8 ⎦

Internally, the program handles matrix with fractions as floating point matrices. To demonstrate this you can use the Insert Into Button and reinsert this matrix into one of of the input boxes. This would then produce the following:

            0.50, 0.83, 0.50
            0.80, 1.60, 0.25
            0.56, 0.44, 0.80

            '''
        elif text == "Vector Definitions":
            text = '''
+------------+
| Addition   |
+------------+

• Vector Addition: The sum of two vectors of the same dimensions is obtained by adding the corresponding entries.

            ⎡3⎤      ⎡1⎤     ⎡4⎤
            ⎣4⎦  +   ⎣2⎦  =  ⎣6⎦

- Commutative property: The order of the vectors being added does not matter. That is, for any two vectors u and v, u + v = v + u.
- Associative property: The way in which three or more vectors are grouped when added does not matter. That is, for any three vectors u, v, and w, (u + v) + w = u + (v + w).
- Identity element: There exists a vector, denoted by 0, such that for any vector u, u + 0 = u.
- Inverse element: For any vector u, there exists a vector -u such that u + (-u) = 0.
- Scalar multiplication: A vector can be multiplied by a scalar (a real number), resulting in a new vector. The scalar multiplication distributes over vector addition, that is, for any scalar k and any two vectors u and v, k(u + v) = ku + kv.


+----------------+
| Dot Product    |
+----------------+

•Dot Product: The dot product of two vectors of the same dimensions is obtained by multiplying the corresponding entries and then summing the results.

- The dot product is only defined for two vectors of the same dimension.
- The dot product is commutative: A · B = B · A
- The dot product is distributive: A · (B + C) = A · B + A · C
- The dot product is associative with scalar multiplication: a(A · B) = (aA) · B = A · (aB)
- The dot product of a vector with itself is equal to the square of its magnitude: A · A = |A|^2
- The dot product can be used to find the angle between two vectors: cosθ = (A · B) / (|A| |B|), where θ is the angle between A and B.
- If the dot product of two vectors is zero, then the vectors are orthogonal (perpendicular) to each other.


+----------------+
| Cross Product  |
+----------------+

•Cross Product: The cross product of two vectors of the same dimensions is obtained by multiplying the corresponding entries and then summing the results.

Here are the rules for the cross product of two vectors:

- The cross product is only defined for vectors in three-dimensional space.
- The cross product is anti-commutative: A × B = -B × A.
- The magnitude of the cross product is equal to the area of the parallelogram formed by the two vectors: |A × B| = |A||B|sinθ, where θ is the angle between the vectors A and B.
- The direction of the cross product is perpendicular to both vectors: A × B is a vector perpendicular to both A and B. The direction is given by the right-hand rule: if you curl the fingers of your right hand in the direction of A, and then curl them toward B, your thumb will point in the direction of A × B.
- If two vectors are parallel or anti-parallel (180 degrees apart), their cross product is zero.
- The cross product is distributive over vector addition: A × (B + C) = A × B + A × C.
- The cross product is not associative: (A × B) × C is not necessarily equal to A × (B × C).
- The cross product can be used to find a vector that is perpendicular to a plane defined by two other vectors: if A and B are two vectors in the plane, then A × B is a vector that is perpendicular to the plane.


+-----------------------+
| Magnitude of a Vector |
+-----------------------+
The magnitude of a vector refers to its length, which can be calculated using the Pythagorean theorem. The rules for vector magnitude are:

For a vector v in n-dimensional space, the magnitude is given by ||v||, where ||v|| is a non-negative scalar value.
The magnitude of a vector is always non-negative and is equal to zero if and only if the vector is a zero vector.
If v = (v1, v2, ..., vn), then ||v|| = sqrt(v1^2 + v2^2 + ... + vn^2).
The magnitude of a vector is invariant under translations, rotations, and reflections of the coordinate system.
Note that the magnitude of a vector is also sometimes referred to as the "norm" or "length" of the vector.

# Example
The norm or magnitude of a vector is the square root of the sum of the squares of its components. For the vector 2,-1,3,-5, the norm can be calculated as follows:

||v|| = sqrt(2^2 + (-1)^2 + 3^2 + (-5)^2)
= sqrt(4 + 1 + 9 + 25)
= sqrt(39)

Therefore, the norm of the vector <2,-1,3,-5> is sqrt(39).

+----------------+
| Projection     |
+----------------+

•Projection: The projection of a vector onto another vector is obtained by multiplying the vector by the dot product of the vector and the other vector divided by the dot product of the other vector and itself.
Vector projection is only defined for vectors of the same dimension

Projection of A onto B (denoted as proj(A, B)): It is the vector that is parallel to B and has the same direction as B. It is calculated as:
proj(A, B) = (A · B) / |B| * (B / |B|), where · denotes the dot product, |B| denotes the magnitude of B, and B / |B| denotes the unit vector in the direction of B.

Projection of B onto A (denoted as proj(B, A)): It is the vector that is parallel to A and has the same direction as A. It is calculated as:
proj(B, A) = (A · B) / |A| * (A / |A|), where · denotes the dot product, |A| denotes the magnitude of A, and A / |A| denotes the unit vector in the direction of A.


+----------------+
| Subtraction    |
+----------------+

•Vector Subtraction: The difference of two vectors of the same dimensions is obtained by subtracting the corresponding entries. 

- To subtract two vectors, you subtract their corresponding components.
- If you have two vectors u and v, then u - v is defined as:

    (u1 - v1, u2 - v2, ..., un - vn)
    where n is the dimension of the vectors.

- Vector subtraction is equivalent to vector addition with the negative of the second vector, i.e., u - v = u + (-v).
- Geometrically, vector subtraction is equivalent to moving from the initial point of the second vector to the terminal point of the first vector.
- Vector subtraction is not commutative, i.e., u - v ≠ v - u in general.
- The zero vector 0 is the additive identity for vector subtraction, i.e., u - 0 = u for any vector u.
- For any vector u, there exists a unique vector -u such that u + (-u) = 0. This is the additive inverse of u.
- Vector subtraction is distributive with respect to scalar multiplication, i.e., a(u - v) = au - av for any scalar a.

- Vector subtraction is not associative, i.e., (u - v) - w ≠ u - (v - w) in general.

+----------------+
| Unit Vector    |
+----------------+

A unit vector is a vector with a magnitude of 1. To obtain a unit vector from a given vector, you need to divide the vector by its magnitude.

The rules for unit vector are:

1. The magnitude of a unit vector is equal to 1.
2. Any non-zero vector can be converted to a unit vector by dividing it by its magnitude.
3. A unit vector can be used to represent the direction of a vector.

In other words, a unit vector is a vector with a magnitude of 1, and it is often used to represent the direction of a vector. To obtain a unit vector from a non-zero vector, you divide the vector by its magnitude. For example, if v = [3, 4], the magnitude of v is sqrt(3^2 + 4^2) = 5, so the unit vector u in the direction of v is u = v/|v| = [3/5, 4/5].



            '''
        self.ui.edtHelp.setPlainText(text)
        
