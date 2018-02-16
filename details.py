import sys,os
from PyQt4 import QtGui
from PyQt4.QtGui import *




class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.name = QtGui.QLabel('Name')
        self.quad_code = QtGui.QLabel('quad_code')
        self.profilePic = QtGui.QLabel('Profile Picture')


        self.nameEdit = QtGui.QLineEdit()

        self.quad_codeEdit = QtGui.QLineEdit()


        self.quad_codeEdit.setEchoMode(QtGui.QLineEdit.Password)

        self.pic = QtGui.QLabel()
        pixmap = QPixmap(os.getcwd() + "//logo.png")
        pixmap = pixmap.scaledToWidth(150)
        self.pic.setPixmap(pixmap)

        self.button1 = QPushButton('Take your Photo', self)
        self.button2 = QPushButton('Save', self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(self.quad_code, 2, 0)
        grid.addWidget(self.quad_codeEdit, 2, 1)


        grid.addWidget(self.profilePic, 3, 0)
        grid.addWidget(self.button1, 3, 1)
        grid.addWidget(self.pic, 3, 2)

        grid.addWidget(self.button2, 6, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        # Create a button in the window



        # connect button to function on_click
        self.button2.clicked.connect(self.on_click)
        self.setWindowTitle('Registration')
        self.show()

    def on_click(self):
        nam = self.nameEdit.text()
        pas = self.quad_codeEdit.text()
        filename = QtGui.QFileDialog.getSaveFileName(self, 'file', 'C:\\reg\\file.txt')
        filenam = "my_drawing.jpg"
        self.pic.save(filenam)
        fname = open(filename, 'w')
        fname.write("name=" + str(nam))
        fname.write("\nquad_code=" + str(pas))
        fname.close()




def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()