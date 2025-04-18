import flet as ft


class View(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()
        # Page stuff
        self._page = page
        self._page.title = "Gestore Corsi edizione 2025"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # Controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # Elementi grafici
        self._title = None
        self.ddPD = None
        self.ddCodins = None
        self.btnPrintCorsiPD = None
        self.btnPrintIscrittiCorsiPD = None
        self.btnPrintIscrittiCodins = None
        self.btnPrintCDSCodins = None
        self.lvTxtOut = None


    def load_interface(self):
        # Titolo
        self._title = ft.Text("Gestore Corsi", color="blue", size=24)
        self._page.controls.append(self._title)
        # Altri elementi grafici
        self.ddPD = ft.Dropdown(label="Periodo didattico",
                                options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")],
                                width=200)
        self.ddCodins = ft.Dropdown(label="Corso",
                                    width=200)
        self._controller.fillddCodins_02()
        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa corsi",
                                                 on_click=self._controller.handlePrintCorsiPD,
                                                 width=300)
        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa numero iscritti",
                                                         on_click=self._controller.handlePrintIscrittiCorsiPD,
                                                         width=300)
        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa iscritti al corso",
                                                        on_click=self._controller.handlePrintIscrittiCodins,
                                                        width=300)
        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa per CDS differenti",
                                                   on_click=self._controller.handlePrintCDSCodins,
                                                   width=300)
        self.lvTxtOut = ft.ListView(expand=True)
        row_01 = ft.Row([self.ddPD, self.btnPrintCorsiPD, self.btnPrintIscrittiCorsiPD],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_02 = ft.Row([self.ddCodins, self.btnPrintIscrittiCodins, self.btnPrintCDSCodins],
                        alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row_01, row_02, self.lvTxtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
