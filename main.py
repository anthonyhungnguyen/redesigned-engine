import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from search import SearchApp

qtCreatorFile = "test.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.username = "system"
        self.password = "hung"
        self.login = False
        self.pushButton_Login.clicked.connect(self.checkValidInfo)
        self.actionSearch.triggered.connect(self.openSearch)

    def checkValidInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if (self.usernameLineEdit.text() == self.username
                and self.passwordLineEdit.text() == self.password):
            msg.setText("Log in successfully")
            msg.setInformativeText("You are now able to query the database")
            msg.setWindowTitle("Successfully")
            msg.setStandardButtons(QMessageBox.Ok)
            self.login = True
        else:
            msg.setText("Your username or password is incorrect")
            msg.setWindowTitle("Failed")
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def openSearch(self):
        self.search_window = SearchApp()
        self.search_window.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
