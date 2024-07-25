import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class UiForm(object):
    def __init__(self):
        self.translator_en = QTranslator()
        self.translator_zh = QTranslator()

    def setup_ui(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        self.form = form
        form.resize(1100, 260)
        form.setMinimumSize(QSize(1100, 260))
        form.setMaximumSize(QSize(1100, 260))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        form.setFont(font)

        # 左上角icon设置
        # 创建QIcon对象并加载图标文件
        # 获取PyInstaller的临时文件夹路径
        def base_path():
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))
            return base_path

        icon = QIcon(os.path.join(base_path(), r"icons\feather\repeat.svg"))
        form.setWindowIcon(icon)

        form.setStyleSheet(u"QPushButton{\n"
                           "	border: 2px solid gray;\n"
                           "	border-radius: 10px;\n"
                           "	padding:0 8px;\n"
                           "}\n"
                           "QPushButton:hover {\n"
                           "	background: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 #5dbfff,stop:1 #558eff);\n"
                           "	color: white\n"
                           "}\n"
                           "QTextBrowser{\n"
                           "	border: 2px solid gray;\n"
                           "	border-radius: 10px;\n"
                           "	padding:0 8px;\n"
                           "	background: white;\n"
                           "}\n"
                           "QLineEdit{\n"
                           "	border: 2px solid gray;\n"
                           "	border-radius: 10px;\n"
                           "	padding:0 8px;\n"
                           "	background: white;\n"
                           "}\n"
                           "QProgressBar {\n"
                           "    border: 2px solid grey;\n"
                           "    border-radius: 5px;\n"
                           "    text-align: center;\n"
                           "}\n"
                           "QProgressBar::chunk {\n"
                           "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 #5dbfff,stop:1 #558eff);\n"
                           "    width: 10px;\n"
                           "    margin: 0.5px;\n"
                           "}")
        self.verticalLayout = QVBoxLayout(form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, -1, 0)
        self.choose_ch = QCheckBox(form)
        self.choose_ch.setObjectName(u"choose_ch")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_ch.sizePolicy().hasHeightForWidth())
        self.choose_ch.setSizePolicy(sizePolicy)
        self.choose_ch.setMinimumSize(QSize(150, 20))
        self.choose_ch.setMaximumSize(QSize(150, 30))
        self.choose_ch.setFont(font)
        self.choose_ch.setChecked(True)
        self.choose_ch.setAutoExclusive(True)
        self.choose_ch.setTristate(False)
        self.horizontalLayout_2.addWidget(self.choose_ch)

        self.choose_en = QCheckBox(form)
        self.choose_en.setObjectName(u"choose_en")
        sizePolicy.setHeightForWidth(self.choose_en.sizePolicy().hasHeightForWidth())
        self.choose_en.setSizePolicy(sizePolicy)
        self.choose_en.setMinimumSize(QSize(150, 20))
        self.choose_en.setMaximumSize(QSize(150, 30))
        self.choose_en.setFont(font)
        self.choose_en.setAutoExclusive(True)

        self.translator_en.load(os.path.join(base_path(), r'translations\en_US.qm'))
        self.choose_en.stateChanged.connect(self.on_language_changed)
        self.translator_zh.load(os.path.join(base_path(), r'translations\zh_CN.qm'))
        QApplication.instance().installTranslator(self.translator_zh)

        self.horizontalLayout_2.addWidget(self.choose_en)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 8)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line = QFrame(form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_7.addWidget(self.line)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, 5)
        self.excel_label = QLabel(form)
        self.excel_label.setObjectName(u"excel_label")
        sizePolicy.setHeightForWidth(self.excel_label.sizePolicy().hasHeightForWidth())
        self.excel_label.setSizePolicy(sizePolicy)
        self.excel_label.setMinimumSize(QSize(150, 25))
        self.excel_label.setMaximumSize(QSize(150, 30))
        self.excel_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.excel_label)

        self.excel_path = QTextBrowser(form)
        self.excel_path.setObjectName(u"excel_path")
        sizePolicy.setHeightForWidth(self.excel_path.sizePolicy().hasHeightForWidth())
        self.excel_path.setSizePolicy(sizePolicy)
        self.excel_path.setMinimumSize(QSize(800, 25))
        self.excel_path.setMaximumSize(QSize(1000, 30))
        self.excel_path.setFont(font)

        self.horizontalLayout_3.addWidget(self.excel_path)

        self.excel_folder = QPushButton(form)
        self.excel_folder.setObjectName(u"excel_folder")
        sizePolicy.setHeightForWidth(self.excel_folder.sizePolicy().hasHeightForWidth())
        self.excel_folder.setSizePolicy(sizePolicy)
        self.excel_folder.setMinimumSize(QSize(80, 25))
        self.excel_folder.setMaximumSize(QSize(80, 30))
        self.excel_folder.setFont(font)

        self.horizontalLayout_3.addWidget(self.excel_folder)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, -1, 5, 5)
        self.txt_label = QLabel(form)
        self.txt_label.setObjectName(u"txt_label")
        self.txt_label.setMinimumSize(QSize(150, 25))
        self.txt_label.setMaximumSize(QSize(150, 30))
        self.txt_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.txt_label)

        self.txt_path = QTextBrowser(form)
        self.txt_path.setObjectName(u"txt_path")
        sizePolicy.setHeightForWidth(self.txt_path.sizePolicy().hasHeightForWidth())
        self.txt_path.setSizePolicy(sizePolicy)
        self.txt_path.setMinimumSize(QSize(800, 25))
        self.txt_path.setMaximumSize(QSize(1000, 30))
        self.txt_path.setFont(font)

        self.horizontalLayout_4.addWidget(self.txt_path)

        self.txt_folder = QPushButton(form)
        self.txt_folder.setObjectName(u"txt_folder")
        sizePolicy.setHeightForWidth(self.txt_folder.sizePolicy().hasHeightForWidth())
        self.txt_folder.setSizePolicy(sizePolicy)
        self.txt_folder.setMinimumSize(QSize(80, 25))
        self.txt_folder.setMaximumSize(QSize(80, 30))
        self.txt_folder.setFont(font)

        self.horizontalLayout_4.addWidget(self.txt_folder)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, -1, 5, 5)
        self.symbol_label = QLabel(form)
        self.symbol_label.setObjectName(u"symbol_label")
        self.symbol_label.setMinimumSize(QSize(150, 25))
        self.symbol_label.setMaximumSize(QSize(150, 30))
        self.symbol_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.symbol_label)

        self.separator_symbol = QLineEdit(form)
        self.separator_symbol.setObjectName(u"separator_symbol")
        sizePolicy.setHeightForWidth(self.separator_symbol.sizePolicy().hasHeightForWidth())
        self.separator_symbol.setSizePolicy(sizePolicy)
        self.separator_symbol.setMinimumSize(QSize(150, 25))
        self.separator_symbol.setMaximumSize(QSize(200, 30))
        self.separator_symbol.setFont(font)

        self.horizontalLayout_5.addWidget(self.separator_symbol)

        self.horizontalSpacer_2 = QSpacerItem(300, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.start_exchange = QPushButton(form)
        self.start_exchange.setObjectName(u"start_exchange")
        sizePolicy.setHeightForWidth(self.start_exchange.sizePolicy().hasHeightForWidth())
        self.start_exchange.setSizePolicy(sizePolicy)
        self.start_exchange.setMinimumSize(QSize(380, 25))
        self.start_exchange.setMaximumSize(QSize(380, 30))
        self.start_exchange.setFont(font)

        self.horizontalLayout_5.addWidget(self.start_exchange)

        self.horizontalSpacer_3 = QSpacerItem(55, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.line_2 = QFrame(form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.progressBar = QProgressBar(form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 25))
        self.progressBar.setMaximumSize(QSize(16777215, 25))
        self.progressBar.setValue(0)

        self.horizontalLayout_6.addWidget(self.progressBar)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.retranslate_ui(form)

        QMetaObject.connectSlotsByName(form)

    def retranslate_ui(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", "Format Conversion Tool", None))
        self.choose_ch.setText(QCoreApplication.translate("form", "Simplified Chinese", None))
        self.choose_en.setText(QCoreApplication.translate("form", "English", None))
        self.excel_label.setText(QCoreApplication.translate("form", "Path to Excel:", None))
        self.excel_path.setHtml(QCoreApplication.translate("form",
                                                           u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                           "p, li { white-space: pre-wrap; }\n"
                                                           "</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                           "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                           None))
        self.excel_folder.setText(QCoreApplication.translate("form", "Browse", None))
        self.txt_label.setText(QCoreApplication.translate("form", "Path to save folder:", None))
        self.txt_path.setHtml(QCoreApplication.translate("form",
                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'\u5fae\u8f6f\u96c5\u9ed1'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                         None))
        self.txt_folder.setText(QCoreApplication.translate("form", "Browse", None))
        self.symbol_label.setText(QCoreApplication.translate("form", "Separator symbol:", None))
        self.start_exchange.setText(QCoreApplication.translate("form", "Start conversion", None))

    def on_language_changed(self):
        if self.choose_en.isChecked():
            # 切换到英文
            QApplication.instance().removeTranslator(self.translator_zh)
            QApplication.instance().installTranslator(self.translator_en)
        else:
            # 切换到中文
            QApplication.instance().removeTranslator(self.translator_en)
            QApplication.instance().installTranslator(self.translator_zh)
        self.retranslate_ui(self.form)
