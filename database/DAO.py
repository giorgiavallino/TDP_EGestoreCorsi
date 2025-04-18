from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT c.codins
                FROM corso c"""
        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(row["codins"])
        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    FROM corso c"""
        cursor.execute(query)
        risultato = []
        for row in cursor:
            risultato.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"])) # si può anche usare
            # direttamente risultato.append(Corso(**row))
        cursor.close()
        cnx.close()
        return risultato

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    FROM corso c
                    WHERE c.pd=%s"""
        cursor.execute(query, (pd,))
        risultato = []
        for row in cursor:
            risultato.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))  # si può anche usare
            # direttamente risultato.append(Corso(**row))
        cursor.close()
        cnx.close()
        return risultato


if __name__ == "__main__":
    print(DAO.getCodins())