import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime  # 区分大小写

from datetime import date, datetime

# 生成orm基类
base = declarative_base()


class Brand(base):
    __tablename__ = 'erp_sppp'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


class Model(base):
    __tablename__ = 'erp_spuxx'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    erp_sppp_id = Column(Integer)
    erp_spfl_id = Column(Integer)
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


# 规格
class Specification(base):
    __tablename__ = 'erp_spgg'  # 表名
    id = Column(Integer, primary_key=True)
    pid = Column(Integer)
    title = Column(String(100))
    erp_spfl_id = Column(Integer)
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


# 商品
class Commodity(base):
    __tablename__ = 'erp_skuxx'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    erp_sppp_id = Column(Integer)
    erp_spfl_id = Column(Integer)
    erp_spuxx_id = Column(Integer)
    erp_spgg_ids = Column(String(200))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

