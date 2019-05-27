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

                