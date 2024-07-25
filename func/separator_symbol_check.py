from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression


class LimitedTextEdit:
    def __init__(self, ui):
        self.ui = ui
        self.separator_symbol = self.ui.separator_symbol
        # 在初始化的时候就进行正则表达式的检验，如果单独设函数，会导致第一次输入无输入检验
        # 创建一个正则表达式，用于检验输入的符号是否符合要求
        regexp = QRegularExpression(r"[@!$%^&*()_+\{\}:\"<>?\[\];\',./\|`-]")
        # 创建一个 QRegularExpressionValidator，使用上面创建的正则表达式
        validator = QRegularExpressionValidator(regexp, self.separator_symbol)
        # 将验证器设置给 QLineEdit
        self.separator_symbol.setValidator(validator)
        self.separator_symbol.setMaxLength(1)
