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
        self.msg = QtGui.QLabel('VisionAid account Registration')

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

        grid.addWidget(self.msg, 1, 0)

        grid.addWidget(self.name, 2, 0)
        grid.addWidget(self.nameEdit, 2, 1)

        grid.addWidget(self.quad_code, 3, 0)
        grid.addWidget(self.quad_codeEdit, 3, 1)


        grid.addWidget(self.profilePic, 4, 0)
        grid.addWidget(self.button1, 4, 1)
        grid.addWidget(self.pic, 4, 2)

        

        grid.addWidget(self.button2, 6, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        # Create a button in the window



        # connect button to function on_click
        self.button1.clicked.connect(self.take_pic)
        # connect button to function on_click
        self.button2.clicked.connect(self.on_click)
        self.setWindowTitle('Registration')
        self.show()

    def on_click(self):
        nam = self.nameEdit.text()
        pas = self.quad_codeEdit.text()
        filename = QtGui.QFileDialog.getSaveFileName(self, 'file', 'C:\\reg\\file.txt')
        fname = open(filename, 'w')
        fname.write("name=" + str(nam))
        fname.write("\nquad_code=" + str(pas))
        fname.write("\npic="+str(nam)+'.jpg')
        fname.close()
        os.system('net user /add ' + str(nam) + ' ' +  str(pas))

        
    
    def take_pic(self):
        import cv2,time
        self.msg.repaint()
        self.msg.setText('Setting camera')
        time.sleep(1)
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        time.sleep(10)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        self.msg.setText('')
        del(camera)
        name = str(self.nameEdit.text())
        cv2.imwrite(name+'.jpg',image)
        pixmap = QPixmap(name +".jpg")
        pixmap = pixmap.scaledToWidth(150)
        self.pic.setPixmap(pixmap)
        self.button1.setText('Retake Photo')
                


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
