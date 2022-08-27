from modules.generator.pages import Page
from ui.gui import Ui_MainWindow


def update_page_text(ui: Ui_MainWindow):
    if ui.page_index.text() == str():
        ui.page_text.setPlainText('')
        return

    try:
        ui.page_text.setPlainText(Page.from_index(int(ui.page_index.text())))
    except:
        ui.page_text.setPlainText('Something went wrong, change index or text here.')
