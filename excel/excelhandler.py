import xlrd
import xlwt
from datetime import date,datetime
from db import dbhandler
from db.dbhandler import brand

#文件地址
file = 'e:\手机0417.xls'

session = dbhandler.create_session()

def read_all_excel():

    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字

    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    #sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    #print(sheet1,sheet2)
    print(sheet1.name,sheet1.nrows,sheet1.ncols)

    #rows = sheet1.row_values(2)#获取行内容
    #cols = sheet1.col_values(3)#获取列内容
    #print(rows)
    #print(cols)

    #print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    #print(sheet1.cell_value(1,0))
    #print(sheet1.row(1)[0].value)

    num_rows = sheet1.nrows
    num_cols = sheet1.ncols
    for rown in range(num_rows):
        for coln in range(num_cols):
            cell = sheet1.cell_value(rown, coln)
            print(cell)

def read_brand_excel():
    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #num_rows = sheet1.nrows
    num_rows = 1
    num_cols = sheet1.ncols
    for rown in range(num_rows):
        cell = sheet1.cell_value(rown, 2)
        print(cell)
        dbhandler.query_brand(session, brand, cell)

read_brand_excel()