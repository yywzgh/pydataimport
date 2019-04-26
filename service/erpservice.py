import xlrd
import xlwt
from datetime import date, datetime
from dao import erpdao
from model.erpmodel import Brand, Model, Specification, Commodity

# 文件地址
file = 'e:\手机0417.xls'

session = erpdao.create_session()


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


# 1.插入品牌
def insert_brand_data():
    wb = xlrd.open_workbook(filename=file)# 打开文件
    print(wb.sheet_names())# 获取所有表格名字
    sheet1 = wb.sheet_by_index(0)# 通过索引获取表格
    print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #num_rows = sheet1.nrows
    num_rows = 2
    num_cols = sheet1.ncols
    for rown in range(1, num_rows):
        brand_name = sheet1.cell_value(rown, 2)
        print(brand_name)
        erpdao.save_brand(session, Brand, brand_name)


# 2.型号
def insert_model_data():
    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    #num_rows = sheet1.nrows
    num_rows = 2
    num_cols = sheet1.ncols
    for rown in range(1, num_rows):
        type_name = sheet1.cell_value(rown, 0)
        type_id = sheet1.cell_value(rown, 1)
        brand_name = sheet1.cell_value(rown, 2)
        brand_id = erpdao.query_brand_id(session, Brand, brand_name)
        print(brand_name)
        model_name = sheet1.cell_value(rown, 3)
        erpdao.save_model(session, Model, model_name, brand_id, type_id)


# 3.插入规格
def insert_specification_data(num_cols, parent_title):
    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    #num_rows = sheet1.nrows
    num_rows = 2
    #num_cols = sheet1.ncols
    for rown in range(1,num_rows):
        type_id = sheet1.cell_value(rown, 1)
        title = sheet1.cell_value(rown, num_cols)
        if title:
            erpdao.save_specification(session, Specification, title, type_id, parent_title)


# 4.商品
def insert_commodity_data():
    wb = xlrd.open_workbook(filename=file)#打开文件
    print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    #num_rows = sheet1.nrows
    num_rows = 2
    num_cols = sheet1.ncols
    for rown in range(1, num_rows):

        type_name = sheet1.cell_value(rown, 0)
        type_id = sheet1.cell_value(rown, 1)

        brand_name = sheet1.cell_value(rown, 2)
        brand_id = erpdao.query_brand_id(session, Brand, brand_name)

        model_name = sheet1.cell_value(rown, 3)
        model_id = erpdao.query_model_id(session, Model, model_name, brand_id, type_id)

        print("型号", model_name, model_id)

        version = sheet1.cell_value(rown, 4)
        version_id = erpdao.query_specification_id(session, Specification, version, type_id)

        print("version_id", version_id)

        storage = sheet1.cell_value(rown, 5)
        storage_id = erpdao.query_specification_id(session, Specification, storage, type_id)
        print("storage", storage_id)

        colour = sheet1.cell_value(rown, 6)
        colour_id = erpdao.query_specification_id(session, Specification, colour, type_id)
        print("###### colour", colour_id)

        spec_ids = version_id.join(storage_id).join(colour_id).strip(",")

        print("--------------",spec_ids)

        commodity_name = sheet1.cell_value(rown, 7)
        commodity_id = sheet1.cell_value(rown, 8)

        erpdao.save_commodity(session, Commodity, commodity_id, commodity_name, brand_id, type_id, model_id, spec_ids)
