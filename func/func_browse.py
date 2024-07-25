from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QCoreApplication


class FuncBrowseButton:
    # 初始化
    def __init__(self, ui, parent_widget=None):
        self.ui = ui
        self.parent_widget = parent_widget

    def select_excel(self):
        # 设置文件过滤器，只显示Excel文件
        filters = "Excel files (*.xls *.xlsx)"
        choose_excel_message = QCoreApplication.translate("MyWindow", "Open Excel File")
        # 使用getOpenFileName，因为它用于选择单个文件
        # getOpenFileName 会返回两个值，变量后面的下划线表示用不到第二个值，故意忽略
        excel_path, _ = QFileDialog.getOpenFileName(self.parent_widget, choose_excel_message, "", filters)
        self.ui.excel_path.setText(excel_path)

    def select_folder(self):
        choose_folder_message = QCoreApplication.translate("MyWindow", "Choose Folder")
        folder_path = QFileDialog.getExistingDirectory(self.parent_widget, choose_folder_message)
        self.ui.txt_path.setText(folder_path)
