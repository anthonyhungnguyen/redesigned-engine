import sys
from PyQt5 import QtCore, QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
from dbs import HospitalOracle

qtCreatorFile = "search.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class SearchApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.hospitalOracle = HospitalOracle()
        self.pushButtonSearch.clicked.connect(self.searchForInfo)

    def searchForInfo(self):
        # Get query from field
        PFNAME = self.patientSFNameLineEdit.text().strip()
        PLNAME = self.patientSLNameLineEdit.text().strip()

        # Store result from Oracle
        storage = self.hospitalOracle.searchPatient(PFNAME, PLNAME)

        # Reset table
        self.tableWidget.setRowCount(0)

        # Insert into table
        for rowPosition, row in enumerate(storage):
            self.tableWidget.insertRow(rowPosition)
            for colPosition, data in enumerate(row):
                self.tableWidget.setItem(rowPosition, colPosition, QtWidgets.QTableWidgetItem(str(data).strip()))
        

        
