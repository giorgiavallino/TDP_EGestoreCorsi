from database.DAO import DAO

class Model:

    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    def getCorsiPDWithIscritti(self, pd):
        return DAO.getCorsiPDWithIscritti(pd)

    def getStudentiCorso(self, codins):
        studenti = DAO.getStudentiCorso(codins)
        studenti.sort(key=lambda studente: studente.cognome) # si possono ordinare gli studenti in base al cognome
        return studenti

    def getCDSofCorso(self, codins):
        cds = DAO.getCDSofCorso(codins)
        cds.sort(key=lambda c: c[1], reverse=True) # ordinamento per numero di studenti iscritti
        return cds