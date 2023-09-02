from PyQt5.QtWidgets import *
from kasatasarim import Ui_MainWindow

class main (QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.qtTasarim = Ui_MainWindow()
        self.qtTasarim.setupUi(self)

app = QApplication([])
pencere = main()
pencere.show()
app.exec_()