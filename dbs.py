import cx_Oracle
from datetime import datetime


class HospitalOracle():
    def __init__(self):
        self.con = cx_Oracle.connect("system", "hung", "xe")
        self.cur = self.con.cursor()
        self.cur.execute('ALTER SESSION SET CURRENT_SCHEMA = HOSPITAL_ADMIN')

    def searchPatient(self, PFNAME, PLNAME):
        query = """SELECT PFNAME, PLNAME, PPHONE, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT FROM (SELECT PID, PFNAME, PLNAME, PPHONE, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, NULL AS TRSTART, NULL AS TREND, NULL AS TRRESULT
            FROM PATIENT 
            JOIN EXAMINATION ON PID=PID_OUT
            UNION
            SELECT PID, PFNAME, PLNAME, PPHONE, NULL AS EXDATE, NULL AS EXFEE, NULL AS EXDIAGNOSIS, NULL AS EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT
            FROM PATIENT
            JOIN TREATMENT ON PID=PID_IN)
            WHERE LTRIM(RTRIM(PFNAME))='""" + PFNAME + """'AND LTRIM(RTRIM(PLNAME))='""" + PLNAME + """'"""
        
        self.cur.execute(query)

        # Store data fetched from cursor
        storage = self.cur.fetchall()
        # initialize variable
        exDate = []
        exFee = []
        exDiagnosis = []
        ex2Date = []
        trStart = []
        trEnd = []
        trResult = []
        pFname = ''
        pLname = ''
        pPhone = ''

        # After fetching, number of rows would increase
        if self.cur.rowcount != 0:
            for pfname, plname, pphone, exdate, exfee, exdiagnosis, ex2date, trstart, trend, trresult in storage:
                if pFname == '':
                    pFname = pfname
                if pLname == '':
                    pLname = plname
                if pPhone == '':
                    pPhone = pphone
                if exdate is not None:
                    exDate.append(exdate.strftime('%m/%d/%Y'))
                if exfee is not None:
                    exFee.append(str(exfee))
                if exdiagnosis is not None:
                    exDiagnosis.append(exdiagnosis[1:])
                if ex2date is not None:
                    ex2Date.append(ex2date.strftime('%m/%d/%Y'))
                if trstart is not None:
                    trStart.append(trstart.strftime('%m/%d/%Y'))
                if trend is not None:
                    trEnd.append(trend.strftime('%m/%d/%Y'))
                if trresult is not None:
                    trResult.append(trresult)
        return pFname, pLname, pPhone, exDate, exFee, exDiagnosis, ex2Date, trStart, trEnd, trResult
