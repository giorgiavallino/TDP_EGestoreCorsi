import flet as ft

class Controller:

    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddCodinsValue = None

    def fillddCodins_01(self):
        codici = self._model.getCodins()
        for codice in codici:
            self._view.ddCodins.options.append(ft.dropdown.Option(codice))
    # --> alla dropdown vengono aggiunte delle stringhe

    def fillddCodins_02(self):
        corsi = self._model.getAllCorsi()
        for corso in corsi:
            self._view.ddCodins.options.append(ft.dropdown.Option(key=corso.codins,
                                                                  data=corso,
                                                                  on_click=self._choiceDDCodins))
    # --> alla dropdown vengono aggiunti degli oggetti Corso

    def _choiceDDCodins(self, e):
        self._ddCodinsValue = e.control.data # in questo modo viene recuperato l'oggetto scelto nel dropdown

    def handlePrintCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione: selezionare un periodo didattico!")
            self._view.update_page()
            return
        if pd =="I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPD = self._model.getCorsiPD(pdInt)
        if len(corsiPD) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato per questo periodo didattico."))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} perido didattico:"))
        for corsoPD in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(corsoPD))
        self._view.update_page()

    def handlePrintIscrittiCorsiPD(self, e):
        self._view.lvTxtOut.controls.clear()
        pd = self._view.ddPD.value
        if pd is None:
            self._view.create_alert("Attenzione: selezionare un periodo didattico!")
            self._view.update_page()
            return
        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2
        corsiPDWithIscritti = self._model.getCorsiPDWithIscritti(pdInt)
        if len(corsiPDWithIscritti) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun corso trovato per questo periodo didattico."))
            self._view.update_page()
            return
        for corsoPDWithIscritti in corsiPDWithIscritti:
            self._view.lvTxtOut.controls.append(ft.Text(f"{corsoPDWithIscritti[0]} - Numero iscritti: {corsoPDWithIscritti[1]}"))
        self._view.update_page()

    def handlePrintIscrittiCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione: selezionare un corso!")
            self._view.update_page()
            return
        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)
        if len(studenti) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessuno studente iscritto a questo corso."))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Sono iscritti al corso {self._ddCodinsValue} {len(studenti)} studenti:"))
        for studente in studenti:
            self._view.lvTxtOut.controls.append(ft.Text(studente))
        self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.lvTxtOut.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Attenzione: selezionare un corso!")
            self._view.update_page()
            return
        cds = self._model.getCDSofCorso(self._ddCodinsValue.codins)
        if len(cds) == 0:
            self._view.lvTxtOut.controls.append(ft.Text("Nessun CDS offre questo corso."))
            self._view.update_page()
            return
        self._view.lvTxtOut.controls.append(ft.Text(f"Iscritti di ciascun CDS che frequentano il corso {self._ddCodinsValue}."))
        for element in cds:
            self._view.lvTxtOut.controls.append(ft.Text(f"CDS: {element[0]} - Numero di iscritti {element[1]}"))
        self._view.update_page()