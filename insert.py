import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from dbs import HospitalOracle

qtCreatorFile = "insert.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class InsertApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hospitalOracle = HospitalOracle()
        self.pushButtonInsert.clicked.connect(self.insertIntoPatient)

    def insertIntoPatient(self):
        PFNAME = self.pFNameLineEdit.text().strip()
        PLNAME = self.pLNameLineEdit.text().strip()
        PDOB = self.pDoBLineEdit.text().strip()
        PGENDER = self.pGenderLineEdit.text().strip()
        PPHONE = self.pPhoneLineEdit.text().strip()
        PADDRESS = self.pAddressLineEdit.text().strip()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        if PFNAME is not None and PLNAME is not None:
            self.hospitalOracle.insertIntoPatient(PFNAME, PLNAME, PDOB, PGENDER, PPHONE, PADDRESS)
            msg.setText("Add patient successfully")
            msg.setWindowTitle("Successfully")
            msg.setStandardButtons(QMessageBox.Ok)
        else:
            msg.setText("You need to enter PFNAME and PLNAME")
            msg.setWindowTitle("Failed")
            msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

