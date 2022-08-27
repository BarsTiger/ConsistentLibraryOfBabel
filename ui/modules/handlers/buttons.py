from ui.modules.updaters.page_index import update_page_text
from ui.gui import Ui_MainWindow


def on_back_button(ui: Ui_MainWindow):
    ui.page_index.setText(str(int(ui.page_index.text()) - 1))
    update_page_text(ui)


def on_next_button(ui: Ui_MainWindow):
    ui.page_index.setText(str(int(ui.page_index.text()) + 1))
    update_page_text(ui)


def on_back_button_press(ui: Ui_MainWindow):
    ui.back_timer.start(10)


def on_back_button_release(ui: Ui_MainWindow):
    ui.back_timer.stop()


def on_next_button_press(ui: Ui_MainWindow):
    ui.next_timer.start(10)


def on_next_button_release(ui: Ui_MainWindow):
    ui.next_timer.stop()
