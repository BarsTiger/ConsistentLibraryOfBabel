from ui.modules.updaters.page_index import update_page_text
from ui.gui import Ui_MainWindow
from PyQt5 import QtGui


def validate_page_index(ui: Ui_MainWindow, event: QtGui.QKeyEvent, old_event):
    old_event(event)
    for char in ui.page_index.text():
        if char not in '0123456789':
            ui.page_index.setText(''.join(c for c in ui.page_index.text() if c in '0123456789'))
            ui.page_index.setCursorPosition(QtGui.QTextCursor.End)
            break

    update_page_text(ui)
