import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.setGeometry(450, 300, 450, 220)
        self.setWindowTitle('Окно с иконкой')
        self.setWindowIcon(QIcon('Death-Star.ico')) 
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

