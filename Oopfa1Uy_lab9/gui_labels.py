import sys
from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QLineEdit,QLabel
from PyQt5.QtGui import QIcon, QFont

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQt Line Edit"
        self.x=200
        self.y=200
        self.width=300
        self.height=300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.textboxlbl = QLabel('Hello World!', self)
        self.textboxlbl.move(120,120)
        self.lbl2 = QLabel('This program is written in Pycharm', self)
        self.lbl2.move(70,140)
        self.show()

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
