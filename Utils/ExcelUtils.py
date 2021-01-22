import os
import xlrd
from xlutils.copy import copy
import json

# file =  os.path.dirname(os.getcwd()) +"/data/test.xls"
file = "/Users/zhangjiale/Desktop/Python/app/data/test.xls"


class Excel():
    def __init__(self, file=file, index=0):
        self.file = file
        self.index = index

    # 获取某一单元格数据
    def getOneCase(self, row, col):  # row  行  col 列
        with xlrd.open_workbook(self.file) as book:
            sheet = book.sheet_by_index(self.index)
            value = sheet.cell_value(row, col)
            # print(value)
            return value

    # 获取某一表中的所有数据
    def getAllcase(self):
        with xlrd.open_workbook(self.file) as book:  # 打开工作簿
            sheet = book.sheet_by_index(self.index)  # 获取内容所处的sheet页
            list = []
            firstValue = sheet.row_values(0)  # 获取第一行数据
            for i in range(1, sheet.nrows):
                dict = {}
                othersValue = sheet.row_values(i)
                for j in range(len(firstValue)):
                    if isinstance(othersValue[j], float):
                        dict[firstValue[j]] = int(othersValue[j])
                    else:
                        dict[firstValue[j]] = othersValue[j]
                list.append(dict)
                # print(list)
            return list

    def writeValue(self):
        with xlrd.open_workbook(self.file) as book:
            copy_book = copy(book)
            copy_table = copy_book.get_sheet(0)
            copy_table.write(1, 2, "haha")
            copy_book.save(self.file)
