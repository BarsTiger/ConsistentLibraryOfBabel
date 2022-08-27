from ui.modules.updaters.page_text import update_page_index
from modules.config import charset
from ui.gui import Ui_MainWindow
from PyQt5 import QtGui


def validate_page_text(ui: Ui_MainWindow, event: QtGui.QKeyEvent, old_event):
    old_event(event)
    for char in ui.page_text.toPlainText():
        if char not in charset:
            ui.page_text.setPlainText(''.join(c for c in ui.page_text.toPlainText() if c in charset))
            ui.page_text.moveCursor(QtGui.QTextCursor.End)
            break

    update_page_index(ui)
