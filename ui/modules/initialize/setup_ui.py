from ui.gui import Ui_MainWindow
from ui.modules.blur import GlobalBlur
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from ui.modules.initialize import handlers


def on_load(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.page_index.setText('0')
    ui.page_index.setMaxLength(2_147_483_647)
    ui.back_timer = QTimer()
    ui.next_timer = QTimer()

    GlobalBlur(MainWindow.winId(), acrylic=True)

    handlers.register_handlers(ui)
