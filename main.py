from PySide6.QtWidgets import QApplication, QWidget
from ui.ui_excel_txt import UiForm
from func.func_browse import FuncBrowseButton
from func.separator_symbol_check import LimitedTextEdit
from func.func_change import FuncStartChange


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = UiForm()
        self.ui.setup_ui(self)
        self.FuncBrowseButton = FuncBrowseButton(self.ui, self)
        self.LimitedTextEdit = LimitedTextEdit(self.ui)
        self.FuncStartChange = FuncStartChange(self.ui, self)
        # 设置按钮的点击事件，分别触发各自的函数
        self.ui.excel_folder.clicked.connect(self.FuncBrowseButton.select_excel)
        self.ui.txt_folder.clicked.connect(self.FuncBrowseButton.select_folder)
        self.ui.start_exchange.clicked.connect(self.FuncStartChange.main_logic)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
