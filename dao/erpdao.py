import sqlalchemy
from sqlalchemy import create_engine
from model.erpmodel import Brand, Model, Specification, Commodity, Dept, DeptRight, Store, StoreRight, UserRight, UserInfo, User
from sqlalchemy.orm import sessionmaker


# 根据品牌名称查询品牌 不存在则新增
def save_brand(session, classobj, title):
    records = session.query(classobj).filter_by(title=title).all()
    if len(records) == 0:
        add_records(session, Brand(title=title, status="1"))
        print("save_brand", title)


# 根据品牌名称查询型号 不存在则新增
def save_model(session, classobj, title, brand_id, type_id):
    records = session.query(classobj).filter_by(title=title, erp_sppp_id=brand_id, erp_spfl_id=type_id).all()
    if len(records) == 0:
        add_records(session, Model(title=title, erp_sppp_id=brand_id, erp_spfl_id=type_id, status="1"))
        print("save_model", title)


# 查询规格 不存在则新增
def save_specification(session, classobj, title, type_id, parent_title):
    records = session.query(classobj).filter_by(title=title, erp_spfl_id=type_id).all()
    if len(records) == 0:
        records = session.query(classobj).filter_by(title=parent_title, pid=0, erp_spfl_id=type_id).all()
        if len(records) == 0:
            add_records(session, Specification(title=parent_title, pid=0, erp_spfl_id=type_id, status="1"))
            pid = session.query(classobj).filter_by(title=parent_title, erp_spfl_id=type_id).all()[0].id
            add_records(session, Specification(title=title, pid=pid, erp_spfl_id=type_id, status="1"))
        else:
            pid = records[0].id
            add_records(session, Specification(title=title, pid=pid, erp_spfl_id=type_id, status="1"))
    print("save_version", records)


# 保存商品
def save_commodity(session, classobj, commodity_id, commodity_name, brand_id, type_id, model_id, spec_ids):
    add_records(session, Commodity(title=commodity_name, id=commodity_id, erp_sppp_id=brand_id, erp_spfl_id=type_id, erp_spuxx_id=model_id,erp_spgg_ids=spec_ids))


def query_brand_id(session, classobj, title):
    record = session.query(classobj).filter_by(title=title).all()[0]
    return record.id


def query_model_id(session, classobj, title, brand_id, type_id):
    record = session.query(classobj).filter_by(title=title, erp_sppp_id=brand_id, erp_spfl_id=type_id).all()[0]
    return record.id


# 查询规格ID
def query_specification_id(session, classobj, title, type_id):
    records = session.query(classobj).filter_by(title=title, erp_spfl_id=type_id).all()
    if len(records) == 0:
        return ""
    else:
        record = records[0]
        return str(record.pid) + "_" + str(record.id) + ","


# 根据部门名称查询部门 不存在则新增
def save_dept(session, classobj, id, title, pid, erp_gsxx_id, level):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, Dept(id=id, title=title, pid=pid, level=level, status="1"))
        print("save_dept", title)

# 根据部门权限名称查询部门权限 不存在则新增
def save_deptright(session, classobj, id, title, erp_gsxx_id, erp_bmxx_ids):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, Model(id=id, title=title, erp_gsxx_id=erp_gsxx_id, erp_bmxx_ids=erp_bmxx_ids))
        print("save_deptright", title)


# 根据仓库名称查询仓库 不存在则新增
def save_store(session, classobj,id, title, pid, erp_gsxx_id, level):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, Store(id=id, title=title, pid=pid, erp_gsxx_id=erp_gsxx_id, level=level, status="1"))
        print("save_store", title)


# 根据部门权限名称查询部门权限 不存在则新增
def save_storeright(session, classobj, id, title, erp_gsxx_id, erp_ckxx_ids):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, StoreRight(id=id, title=title, erp_gsxx_id=erp_gsxx_id, erp_ckxx_ids=erp_ckxx_ids))
        print("save_storeright", title)


# 根据仓库名称查询仓库 不存在则新增
def save_userright(session, classobj, id, erp_ckqx_id, erp_bmqx_id):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, UserRight(id=id, erp_ckqx_id=erp_ckqx_id, erp_bmqx_id=erp_bmqx_id, status="1"))
        print("save_userright", id)


def save_userinfo(session, classobj, id, full_name, mobile, erp_gsxx_id, erp_bmxx_id):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, UserInfo(id=id, full_name=full_name, mobile=mobile, erp_gsxx_id=erp_gsxx_id, erp_bmxx_id=erp_bmxx_id, status="1"))
        print("save_userinfo", id)


def save_user(session, classobj, id, username, real_name, erp_gsxx_id):
    records = session.query(classobj).filter_by(id=id).all()
    if len(records) == 0:
        add_records(session, User(id=id, username=username, real_name=real_name, erp_gsxx_id=erp_gsxx_id, status="1"))
        print("save_userinfo", id)


def add_records(session, classobj):
    if isinstance(classobj, list):
        session.add_all(classobj)
    else:
        session.add(classobj)
    session.commit()


def add_records(session, classobj):
    if isinstance(classobj, list):
        session.add_all(classobj)
    else:
        session.add(classobj)
    session.commit()


# 创建连接
def create_session():
    # base.metadata.create_all(engine) #创建表结构
    engine = create_engine("mysql+pymysql://root:123456@11.22.33.44:55/test", encoding='utf-8', echo=True)
    session_class = sessionmaker(bind=engine)  ##创建与数据库的会话，class,不是实例
    session = session_class()  # 生成session实例
    return session

# user_obj = brand(title="rr",status="1") #插入你要创建的数据对象，每执行一次都会新增一次数据。
# session.add(user_obj)  #把要创建的数据对象添加到这个session里
# session.commit() #提交，使前面修改的数据生效。


# query_brand(session,brand, '华为融合产品')
