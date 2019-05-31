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
        PDOBLIST = PDOB.split('-')
        WillInsert = True
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        if PFNAME is '' or PLNAME is '' or PGENDER is '' or PPHONE is '' or PADDRESS is '':
            msg.setText("All fields must not be empty")
            msg.setWindowTitle("Failed")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            WillInsert=False

        if (len(PDOBLIST) != 3 or len(PDOBLIST[0]) != 4 or len(PDOBLIST[1]) != 2 or len(PDOBLIST[2]) != 2 or int(PDOBLIST[1]) > 12 or int(PDOBLIST[1]) < 0 or int(PDOBLIST[2]) < 0 or int(PDOBLIST[2]) > 31):
            msg.setText("Please enter date of birth correctly")
            msg.setWindowTitle("Failed")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            WillInsert=False

        if WillInsert:
            self.hospitalOracle.insertIntoPatient(PFNAME, PLNAME, PDOB, PGENDER, PPHONE, PADDRESS)
            msg.setText("Add patient successfully")
            msg.setWindowTitle("Successfully")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()