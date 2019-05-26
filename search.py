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
        self.PFNAME = self.patientSFirstNameLineEdit.text().strip()
        self.PLNAME = self.patientSLastNameLineEdit.text().strip()

        # Execute function
        pFname, pLname, pPhone, exDate, exFee, exDiagnosis, ex2Date, trStart, trEnd, trResult = self.hospitalOracle.searchPatient(
            self.PFNAME, self.PLNAME)

        # Update field
        self.pSFNameLineEdit.setText(pFname)
        self.pSLNameLineEdit.setText(pLname)
        self.pSPNumberLineEdit.setText(pPhone)
        self.examinationSDiagnosisLineEdit.setText(
            'Not Found' if len(exDiagnosis) == 0 else ', '.join(
                x for x in exDiagnosis))
        self.examinationSFeeLineEdit.setText(
            'Not Found' if len(exFee) == 0 else ', '.join(x for x in exFee))
        self.examinationSSecondDateLineEdit.setText(
            'Not Found' if len(ex2Date) == 0 else ', '.join(x
                                                        for x in ex2Date))
        self.examniationSDateLineEdit.setText(
            'Not Found' if len(exDate) == 0 else ', '.join(x for x in exDate))
        self.treatmentSStartDateLineEdit.setText(
            'Not Found' if len(trStart) == 0 else ', '.join(x
                                                            for x in trStart))
        self.treatmentSEndDateLineEdit.setText(
            'Not Found' if len(trEnd) == 0 else ', '.join(x for x in trEnd))
        self.treatmentResultLineEdit.setText('Not Found' if len(trResult) ==
                                             0 else ', '.join(
                                                 x for x in trResult))
