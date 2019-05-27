import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from dbs import HospitalOracle

qtCreatorFile = "list.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ListApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hospitalOracle = HospitalOracle()
        self.pushButtonSearchPatients.clicked.connect(self.searchPatients)

    def searchPatients(self):
        # Get input
        DFNAME = self.doctorSFNameLineEdit.text().strip()
        DLNAME = self.doctorSLNameLineEdit.text().strip()

        # Ger data from table
        storage = self.hospitalOracle.listPatientTreatedByDoctor(DFNAME, DLNAME)

        # Reset all rows
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)
        
        # Insert to 2 tables
        rowOut = 0
        rowIn = 0
        listOut = [0,1,2,3,4,5,6,7,8]
        listIn = [0,1,2,3,4,9,10,11]
        for row in storage:
            if row[5] is not None:
                colPositionOut = 0
                self.tableWidget.insertRow(rowOut)
                for posOut in listOut:
                    self.tableWidget.setItem(rowOut, colPositionOut, QtWidgets.QTableWidgetItem(str(row[posOut]).strip()))
                    colPositionOut += 1
                rowOut += 1
            else:
                colPositionIn = 0
                self.tableWidget_2.insertRow(rowIn)
                for posIn in listIn:
                    print(posIn)
                    print(row[posIn])
                    self.tableWidget_2.setItem(rowIn, colPositionIn, QtWidgets.QTableWidgetItem(str(row[posIn]).strip()))
                    colPositionIn += 1
                rowIn += 1
