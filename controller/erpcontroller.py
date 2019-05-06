from service import erpservice


def import_commodity_data():
    # erpservice.insert_specification_data(4,"规格")
    # erpservice.insert_specification_data(5,"容量")
    # erpservice.insert_specification_data(6,"颜色")
    erpservice.insert_commodity_data()


def import_user_data():
    # erpservice.insert_specification_data(4,"规格")
    # erpservice.insert_specification_data(5,"容量")
    # erpservice.insert_specification_data(6,"颜色")
    erpservice.insert_dept_1_data()
    erpservice.insert_dept_2_data()
    erpservice.insert_dept_3_data()
    erpservice.insert_deptright_data()
    erpservice.insert_store_1_data()
    erpservice.insert_store_2_data()
    erpservice.insert_store_3_data()
    erpservice.insert_storeright_data()

    erpservice.insert_userinfo_data()
    erpservice.insert_userright_data()
    erpservice.insert_user_data()