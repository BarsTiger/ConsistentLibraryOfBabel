from ui.modules import validators
from ui.modules.handlers import buttons
from ui.gui import Ui_MainWindow


def register_handlers(ui: Ui_MainWindow):
    old_page_text_key_press_event = ui.page_text.keyPressEvent
    ui.page_text.keyPressEvent = lambda event: validators.validate_page_text(ui, event, old_page_text_key_press_event)
    old_page_index_key_press_event = ui.page_index.keyPressEvent
    ui.page_index.keyPressEvent = lambda event: validators.validate_page_index(ui, event,
                                                                               old_page_index_key_press_event)

    ui.back_timer.timeout.connect(lambda: buttons.on_back_button(ui))
    ui.next_timer.timeout.connect(lambda: buttons.on_next_button(ui))

    ui.back_button.pressed.connect(lambda: buttons.on_back_button_press(ui))
    ui.back_button.released.connect(lambda: buttons.on_back_button_release(ui))
    ui.next_button.pressed.connect(lambda: buttons.on_next_button_press(ui))
    ui.next_button.released.connect(lambda: buttons.on_next_button_release(ui))
