from modules.generator.pages import Index
from ui.gui import Ui_MainWindow


def update_page_index(ui: Ui_MainWindow):
    ui.page_index.setText(str(Index.from_page(ui.page_text.toPlainText())))
