from database.DB_connect import DBConnect
from model.corso import Corso
from model.studente import Studente

class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.codins
                    FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                risultato.append(row["codins"])
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getAllCorsi():
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM corso c"""
            cursor.execute(query)
            for row in cursor:
                risultato.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"])) # si può anche usare
                # direttamente risultato.append(Corso(**row))
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getCorsiPD(pd):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                    FROM corso c
                    WHERE c.pd=%s"""
            cursor.execute(query, (pd,))
            for row in cursor:
                risultato.append(Corso(row["codins"], row["crediti"], row["nome"], row["pd"]))  # si può anche usare
                # direttamente risultato.append(Corso(**row))
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getCorsiPDWithIscritti(pd):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT c.codins, c.crediti, c.nome, c.pd, COUNT(*) AS n
                    FROM corso c, iscrizione i
                    WHERE c.codins=i.codins AND c.pd=%s
                    GROUP BY c.codins, c.crediti, c.nome, c.pd"""
            cursor.execute(query, (pd,))
            for row in cursor:
                risultato.append((Corso(row["codins"], row["crediti"], row["nome"], row["pd"]), row["n"])) # è una
                # tupla: il primo elemento è un oggetto di tipo Corso, il secondo un numero che rappresenta gli
                # iscritti totali al corso
            cursor.close()
            cnx.close()
            return risultato

    @staticmethod
    def getStudentiCorso(codins):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.*
                    FROM studente s, iscrizione i
                    WHERE s.matricola=i.matricola AND i.codins=%s"""
            cursor.execute(query, (codins,))
            for row in cursor:
                risultato.append(Studente(row["matricola"], row["cognome"], row["nome"], row["CDS"]))
            cursor.close()
            cnx.close()
            return risultato

    def getCDSofCorso(codins):
        cnx = DBConnect.get_connection()
        risultato = []
        if cnx is None:
            return risultato
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.CDS, COUNT(*) AS n
                    FROM studente s, iscrizione i
                    WHERE s.matricola=i.matricola AND i.codins=%s AND s.CDS != ""
                    GROUP BY s.CDS"""
            # Ci sono dei valori CDS vuoti nel database: fare attenzione e seguire le istruzioni dell'esercizio --> in
            # questo caso vengono tralasciati
            cursor.execute(query, (codins,))
            for row in cursor:
                risultato.append((row["CDS"], row["n"]))
            cursor.close()
            cnx.close()
            return risultato

if __name__ == "__main__":
    print(DAO.getCodins())