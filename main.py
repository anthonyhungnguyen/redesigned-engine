import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from search import SearchApp
from insert import InsertApp
from listP import ListApp
from report import ReportApp

qtCreatorFile = "main.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.username = "manager"
        self.password = "hung"
        self.pushButton_Login.clicked.connect(self.checkValidInfo)
        self.actionSearch.triggered.connect(self.openSearch)
        self.actionInput.triggered.connect(self.openInsert)
        self.actionList.triggered.connect(self.openList)
        self.actionReport.triggered.connect(self.openReport)
        self.actionLogout.triggered.connect(self.logOut)
        self.search_window = SearchApp()
        self.insert_window = InsertApp()
        self.list_window = ListApp()
        self.report_window = ReportApp()

    def checkValidInfo(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if (self.usernameLineEdit.text() == self.username
                and self.passwordLineEdit.text() == self.password):
            msg.setText("Log in successfully")
            msg.setInformativeText("You are now able to query the database")
            msg.setWindowTitle("Successfully")
            msg.setStandardButtons(QMessageBox.Ok)
            self.actionSearch.setEnabled(True)
            self.actionInput.setEnabled(True)
            self.actionList.setEnabled(True)
            self.actionReport.setEnabled(True)
            self.actionLogout.setEnabled(True)
            self.usernameLineEdit.setText('')
            self.passwordLineEdit.setText('')
        else:
            msg.setText("Your username or password is incorrect")
            msg.setWindowTitle("Failed")
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def openSearch(self):
        self.search_window.show()
    
    def openInsert(self):
        self.insert_window.show()

    def openList(self):
        self.list_window.show()
    
    def openReport(self):
        self.report_window.show()

    def logOut(self):
        self.search_window.close()
        self.insert_window.close()
        self.list_window.close()
        self.report_window.close()
        self.actionSearch.setEnabled(False)
        self.actionInput.setEnabled(False)
        self.actionList.setEnabled(False)
        self.actionReport.setEnabled(False)
        self.actionLogout.setEnabled(False)
        self.usernameLineEdit.setText('')
        self.passwordLineEdit.setText('')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
