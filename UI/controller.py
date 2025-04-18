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
    # alla dropdown vengono aggiunte delle stringhe

    def fillddCodins_02(self):
        corsi = self._model.getAllCorsi()
        for corso in corsi:
            self._view.ddCodins.options.append(ft.dropdown.Option(key=corso.codins,
                                                                  data=corso,
                                                                  on_click=self._choiceDDCodins))
    # alla dropdown vengono aggiunti degli oggetti Corso

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
        self._view.lvTxtOut.controls.append(ft.Text(f"Corsi del {pd} perido didattico:"))
        for corsoPD in corsiPD:
            self._view.lvTxtOut.controls.append(ft.Text(corsoPD))
        self._view.update_page()


    def handlePrintIscrittiCorsiPD(self, e):
        pass

    def handlePrintIscrittiCodins(self, e):
        pass

    def handlePrintCDSCodins(self, e):
        pass