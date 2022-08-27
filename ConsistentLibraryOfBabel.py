from ui.gui import Ui_MainWindow
from PyQt5 import QtWidgets
from ui.modules.initialize import setup_ui
import sys

sys.setrecursionlimit(2_147_483_647)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_ui.on_load(ui, MainWindow)

MainWindow.show()

sys.exit(app.exec_())
