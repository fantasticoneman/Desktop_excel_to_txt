import os
from datetime import datetime
import pandas as pd
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QMessageBox


class FuncStartChange:
    def __init__(self, ui, parent_widget=None):
        self.ui = ui
        self.excel_path = self.ui.excel_path
        self.txt_path = self.ui.txt_path
        self.separator_symbol = self.ui.separator_symbol
        self.completed_tasks = 0
        self.total_tasks = 0
        self.parent_widget = parent_widget

    def check_file(self):
        # 设置翻译字段
        error_title = QCoreApplication.translate("MyWindow", "Error")
        error_excel_message = QCoreApplication.translate("MyWindow", "Need to choose excel!")
        error_txt_message = QCoreApplication.translate("MyWindow", "Need to choose folder!")
        # 判断excel路径是否为空
        if self.excel_path.toPlainText() == '':
            QMessageBox.warning(self.parent_widget, error_title, error_excel_message)
            check_status = False
        # 判断文本路径是否为空
        elif self.txt_path.toPlainText() == '':
            QMessageBox.warning(self.parent_widget, error_title, error_txt_message)
            check_status = False
        else:
            check_status = True
        return check_status

    # 进度函数
    def update_progress(self):
        success_title = QCoreApplication.translate("MyWindow", "Success")
        success_message = QCoreApplication.translate("MyWindow", "Conversion completion!")
        self.completed_tasks += 1
        progress = (self.completed_tasks / self.total_tasks) * 100
        # 将百分比传到进度条
        self.ui.progressBar.setValue(progress)
        # 进度条到100%，提示完成
        if progress == 100:
            QMessageBox.information(self.parent_widget, success_title, success_message)

    def main_logic(self):
        self.ui.progressBar.setValue(0)
        if self.check_file():
            self.total_tasks = 5
            self.completed_tasks = 0  # 已完成任务数
            # 获取文件扩展名
            _, result = os.path.splitext(self.excel_path.toPlainText())
            # 更新进度
            self.update_progress()
            # 根据excel的扩展名判断进xlrd或者openpyxl
            if result.lower() == '.xls':
                result_data = pd.read_excel(r'%s' % self.excel_path.toPlainText(), engine='xlrd')
            elif result.lower() == '.xlsx':
                result_data = pd.read_excel(r'%s' % self.excel_path.toPlainText(), engine='openpyxl')
            else:
                return
            # 更新进度
            self.update_progress()

            def print_number(result_data):
                if '数量' in result_data.columns:
                    result_data = result_data.rename(columns={'数量': 'num'})
                    result_data['num'] = result_data['num'].astype(int)
                elif 'Number of prints' in result_data.columns:
                    result_data = result_data.rename(columns={'Number of prints': 'num'})
                    result_data['num'] = result_data['num'].astype(int)
                else:
                    # 新增一列每行数据都是1
                    result_data['num'] = 1
                return result_data

            # 对dataframe里面的打印数量列进行处理
            result_data = print_number(result_data)
            # 更新进度
            self.update_progress()

            # 将剩下的列的每行的值用连接符号拼接并转成sting
            result_data['合并'] = result_data.drop('num', axis=1).apply(
                lambda x: '%s' % self.separator_symbol.text().join(x.astype(str)), axis=1)
            # 将拼接后的列跟数量列合并成一个新的dataframe
            final_data = result_data[['合并', 'num']]
            # 更新进度
            self.update_progress()
            # 获取当前时间并格式化为字符串
            current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            # 覆盖写入文本
            with open(r'%s\%s.txt' % (self.txt_path.toPlainText(), current_time), 'w', encoding='utf-8') as file:
                # 遍历DataFrame对象的每一行，index为行号，从零开始；row为每行的内容
                for index, row in final_data.iterrows():
                    # 覆盖写入拼接后的每行内容，该内容重复写入对应行的数量，直至下一行
                    file.write((row['合并'] + '\n') * row['num'])
            # 更新进度
            self.update_progress()
