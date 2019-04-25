import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String  # 区分大小写
from sqlalchemy.orm import sessionmaker

# 生成orm基类
base = declarative_base()


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
    add_records(session, Commodity(title=commodity_name, id=commodity_id, erp_sppp_id=brand_id, erp_spfl_id=type_id, erp_spuxx_id=model_id,erp_spgg_ids=spec_ids, status="1"))


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
        print("##############",record.pid, record.pid)
        return str(record.pid) + "_" + str(record.id) + ","


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


class Brand(base):
    __tablename__ = 'erp_sppp'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    status = Column(String(20))


class Model(base):
    __tablename__ = 'erp_spuxx'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    erp_sppp_id = Column(Integer)
    erp_spfl_id = Column(Integer)
    status = Column(String(20))


# 规格
class Specification(base):
    __tablename__ = 'erp_spgg'  # 表名
    id = Column(Integer, primary_key=True)
    pid = Column(Integer)
    title = Column(String(100))
    erp_spfl_id = Column(Integer)
    status = Column(String(20))


# 商品
class Commodity(base):
    __tablename__ = 'erp_skuxx'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    erp_sppp_id = Column(Integer)
    erp_spfl_id = Column(Integer)
    erp_spuxx_id = Column(Integer)
    erp_spgg_ids = Column(String(200))
    status = Column(String(20))


# 创建连接
def create_session():
    # base.metadata.create_all(engine) #创建表结构

    session_class = sessionmaker(bind=engine)  ##创建与数据库的会话，class,不是实例
    session = session_class()  # 生成session实例
    return session

# user_obj = brand(title="rr",status="1") #插入你要创建的数据对象，每执行一次都会新增一次数据。
# session.add(user_obj)  #把要创建的数据对象添加到这个session里
# session.commit() #提交，使前面修改的数据生效。


# query_brand(session,brand, '华为融合产品')
