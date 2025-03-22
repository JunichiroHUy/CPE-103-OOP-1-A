import sys

from PyQt5.QtWidgets import QWidget,QApplication,QMainWindow,QPushButton,QLineEdit,QLabel,QMessageBox,QVBoxLayout
from PyQt5.QtGui import QIcon, QFont



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "Account Registration System"
        self.x=715
        self.y=270
        self.width=480
        self.height=550
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.title = QLabel('*ALL FIELDS ARE REQUIRED*', self)
        self.title.move(20,20)
        self.title.setFont(QFont('Arial', 15, QFont.Bold))

        self.question1 = QLabel('First name:', self)
        self.question1.move(20, 70)
        self.question1.setFont(QFont('Arial', 15))

        self.answer1 = QLineEdit(self)
        self.answer1.move(140, 70)
        self.answer1.resize(300, 30)

        self.question2 = QLabel('Last name:', self)
        self.question2.move(20, 130)
        self.question2.setFont(QFont('Arial', 15))

        self.answer2 = QLineEdit(self)
        self.answer2.move(140, 130)
        self.answer2.resize(300, 30)

        self.question3 = QLabel('Username:', self)
        self.question3.move(20, 190)
        self.question3.setFont(QFont('Arial', 15))

        self.answer3 = QLineEdit(self)
        self.answer3.move(140, 190)
        self.answer3.resize(300, 30)

        self.question4 = QLabel('Password:', self)
        self.question4.move(20, 250)
        self.question4.setFont(QFont('Arial', 15))

        self.answer4 = QLineEdit(self)
        self.answer4.move(140, 250)
        self.answer4.resize(300, 30)

        self.question5 = QLabel('Email Address:', self)
        self.question5.move(20, 310)
        self.question5.setFont(QFont('Arial', 11, QFont.Bold))

        self.answer5 = QLineEdit(self)
        self.answer5.move(140, 310)
        self.answer5.resize(300, 30)

        self.question6 = QLabel('Contact No.:', self)
        self.question6.move(20, 370)
        self.question6.setFont(QFont('Arial', 15))

        self.answer6 = QLineEdit(self)
        self.answer6.move(140, 370)
        self.answer6.resize(300, 30)

        self.subtn = QPushButton('Submit', self)
        self.subtn.move(50,450)
        self.subtn.setGeometry(20, 450, 200, 50)
        self.subtn.setFont(QFont('Arial', 10, QFont.Bold))
        self.subtn.clicked.connect(self.submit)


        self.clearbtn = QPushButton('Clear', self)
        self.clearbtn.move(50, 450)
        self.clearbtn.setGeometry(250, 450, 200, 50)
        self.clearbtn.setFont(QFont('Arial', 10, QFont.Bold))
        self.clearbtn.clicked.connect(self.clear)
        self.show()

    def clear(self):
        self.answer1.clear()
        self.answer2.clear()
        self.answer3.clear()
        self.answer4.clear()
        self.answer5.clear()
        self.answer6.clear()

    def submit(self):
        first_name = self.answer1.text()
        last_name = self.answer2.text()
        user = self.answer3.text()
        password = self.answer4.text()
        email = self.answer5.text()
        contact = self.answer5.text()

        message = (f"INPUT SUBMITTED: You are {first_name}, {last_name}. The username you chose is {user} and your password is [{password}]. Your contact details are {email} and {contact}. Don't forget and make sure to take a screenshot!")
        print(message)

if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
