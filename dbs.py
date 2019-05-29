import cx_Oracle
from datetime import datetime


class HospitalOracle():
    def __init__(self):
        self.con = cx_Oracle.connect("system", "hung", "xe")
        self.cur = self.con.cursor()
        self.cur.execute('ALTER SESSION SET CURRENT_SCHEMA = HOSPITAL_ADMIN')

    def searchPatient(self, PFNAME, PLNAME):
        querySelect = """SELECT PFNAME, PLNAME, PPHONE, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT FROM (SELECT PID, PFNAME, PLNAME, PPHONE, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, NULL AS TRSTART, NULL AS TREND, NULL AS TRRESULT
            FROM PATIENT 
            JOIN EXAMINATION ON PID=PID_OUT
            UNION
            SELECT PID, PFNAME, PLNAME, PPHONE, NULL AS EXDATE, NULL AS EXFEE, NULL AS EXDIAGNOSIS, NULL AS EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT
            FROM PATIENT
            JOIN TREATMENT ON PID=PID_IN)
            WHERE LTRIM(RTRIM(PFNAME))='{}'AND LTRIM(RTRIM(PLNAME))='{}'""".format(PFNAME, PLNAME)
        
        self.cur.execute(querySelect)

        # Store data fetched from cursor
        storage = self.cur.fetchall()
        
        return storage

    def insertIntoPatient(self, PFNAME, PLNAME, PDOB, PGENDER, PPHONE, PADDRESS):
        queryInsert = """BEGIN
                            INSERT_INTO_PATIENT('{}','{}',TO_DATE('{}', 'yyyy/mm/dd'),'{}','{}','{}');
                         END;
                            """.format(PFNAME, PLNAME, PDOB, PGENDER, PPHONE, PADDRESS)
        print(queryInsert)
        self.cur.execute(queryInsert)
        self.con.commit()
    
    def listPatientTreatedByDoctor(self, DFNAME, DLNAME):
        queryList = """SELECT PID ,PFNAME, PLNAME, PPHONE, PDOB, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT FROM (SELECT EID_DOC, PID, PFNAME, PLNAME, PPHONE, PDOB, EXDATE, EXFEE, EXDIAGNOSIS, EXSECONDEXAMINATIONDATE, NULL AS TRSTART, NULL AS TREND, NULL AS TRRESULT
            FROM PATIENT 
            JOIN EXAMINATION ON PID=PID_OUT
            UNION
            SELECT EID_DOC, PID, PFNAME, PLNAME, PPHONE, PDOB, NULL AS EXDATE, NULL AS EXFEE, NULL AS EXDIAGNOSIS, NULL AS EXSECONDEXAMINATIONDATE, TRSTART, TREND, TRRESULT
            FROM PATIENT
            JOIN TREATMENT ON PID=PID_IN)
            WHERE EID_DOC IN (SELECT EID FROM EMPLOYEE WHERE LTRIM(RTRIM(EFNAME))='{}' AND LTRIM(RTRIM(ELNAME))='{}')
            """.format(DFNAME, DLNAME)

        self.cur.execute(queryList)

        storage = self.cur.fetchall()

        return storage

    def makeAReport(self, PFNAME, PLNAME):
        queryReport = """SELECT * FROM (SELECT P.PID, E.EXID, E.EXDATE, E.EXFEE, NULL AS TRID , NULL AS TRSTART, NULL AS TREND, M.MPRICE, NULL AS PFEE, SUM(MPRICE + EXFEE) AS OUTPAYMENT, NULL AS INPAYMENT  FROM PATIENT P
JOIN OUTPATIENT OP ON PID_OUT=PID
JOIN EXAMINATION E ON E.PID_OUT=OP.PID_OUT 
JOIN USES_EXAM UE ON (UE.PID_OUT=E.PID_OUT AND E.EID_DOC=UE.EID_DOC) JOIN MEDICATION M ON UE.MID=M.MID
GROUP BY P.PID, E.EXID, E.EXDATE, M.MPRICE,E.EXFEE
UNION
SELECT P.PID, NULL AS EXID, NULL AS EXDATE, NULL AS EXFEE, T.TRID, T.TRSTART, T.TREND, M.MPRICE, PFEE, NULL AS OUTPAYMENT, SUM(MPRICE + PFEE) AS INPAYMENT FROM PATIENT P
JOIN INPATIENT IP ON PID_IN=PID
JOIN TREATMENT T ON T.PID_IN=IP.PID_IN 
JOIN USES_TREAT UT ON (UT.PID_IN=T.PID_IN AND T.EID_DOC=UT.EID_DOC) JOIN MEDICATION M ON UT.MID=M.MID
GROUP BY P.PID, T.TRID, T.TRSTART, T.TREND, M.MPRICE, PFEE)
WHERE PID IN (SELECT PID FROM PATIENT WHERE LTRIM(RTRIM(PFNAME))='{}' AND LTRIM(RTRIM(PLNAME))='{}')""".format(PFNAME, PLNAME)
        print(queryReport)
        self.cur.execute(queryReport)

        storage = self.cur.fetchall()

        return storage
                