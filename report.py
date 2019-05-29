import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from dbs import HospitalOracle

qtCreatorFile = "report.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class ReportApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hospitalOracle = HospitalOracle()
        self.pushButtonSearch.clicked.connect(self.showReport)

    def showReport(self):
        PFNAME = self.patientSFNameLineEdit.text().strip()
        PLNAME = self.patientSLNameLineEdit.text().strip()

        storage = self.hospitalOracle.makeAReport(PFNAME, PLNAME)

        # Reset table
        self.tableWidget.setRowCount(0)
        self.tableWidget_2.setRowCount(0)

        rowOut = 0
        rowIn = 0
        listOut = [0,1,2,3,7,9]
        listIn = [0,4,5,6,7,8,10]
        for row in storage:
            if row[1] is not None:
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
                    self.tableWidget_2.setItem(rowIn, colPositionIn, QtWidgets.QTableWidgetItem(str(row[posIn]).strip()))
                    colPositionIn += 1
                rowIn += 1
