import xlrd
from xlutils.copy import copy
# xlutils：一般是表是存在的；
# xlwt：是新建表

'''
# 打开excel
excel_path = '../../data/在线考试系统接口测试用例.xls'
workBook = xlrd.open_workbook(excel_path, formatting_info=True)

# 指定对应的sheet
sheetNames = workBook.sheet_names()      # 返回的是列表
workSheet = workBook.sheet_by_name('1-登录模块')

# 读取里面的数据
cell = workSheet.cell(2, 8).value
'''

# 对执行Excel表格操作进行封装


class ExecuteExcel():

    def __init__(self, pathname):
        self.path = pathname

    # 打开Excel表格
    def open_excel(self):
        try:
            path = self.path
            self.workbook = xlrd.open_workbook(path, formatting_info=True)
            return self.workbook
        except Exception as error:
            return error

    # 读取Excel里的数据
    def get_data(self, sheetname, rows=0, cols=0):
        workSheet = self.workbook.sheet_by_name(sheetname)
        value = workSheet.cell(rows, cols).value
        return value

    # 写入数据到Excel里
    def write_data(self):
        newWorkBook = copy(self.workbook)       # 拷贝出来
        newSheet = newWorkBook.get_sheet(1)     # 去对应的表
        return newWorkBook, newSheet


if __name__ == '__main__':
    excel_path = '../../data/在线考试系统接口测试用例.xls'
    excel = ExecuteExcel(excel_path)
    # print(excel.path)     #excel文件地址为对象的初始化属性
    excel.open_excel()
    data = excel.get_data('1-登录模块', 1, 8)       # 读数据
    # print(data)

    # print(excel.write_data())        返回为元组类型
    workbook, sheet = excel.write_data()      # 指定的表格
    sheet.write(1, 10, 'test')
    workbook.save('./res.xls')


