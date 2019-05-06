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

# 部门
class Dept(base):
    __tablename__ = 'erp_bmxx'  # 表名
    id = Column(Integer, primary_key=True)
    erp_gsxx_id = Column(Integer, default=1003)
    pid = Column(Integer)
    title = Column(String(100))
    type = Column(String(100))
    address = Column(String(200))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

# 部门权限
class DeptRight(base):
    __tablename__ = 'erp_bmqx'  # 表名
    id = Column(Integer, primary_key=True)
    erp_gsxx_id = Column(Integer, default=1003)
    title = Column(String(100))
    erp_bmxx_ids = Column(String(200))
    sort = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

# 仓库
class Store(base):
    __tablename__ = 'erp_ckxx'  # 表名
    id = Column(Integer, primary_key=True)
    erp_gsxx_id = Column(Integer, default=1003)
    pid = Column(Integer)
    title = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)

# 仓库权限
class StoreRight(base):
    __tablename__ = 'erp_bmqx'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    erp_gsxx_id = Column(Integer, default=1003)
    erp_ckxx_ids = Column(String(200))
    sort = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


# 用户权限
class UserRight(base):
    __tablename__ = 'erp_ryqx'  # 表名
    id = Column(Integer, primary_key=True)
    erp_ckqx_id = Column(Integer)
    erp_bmqx_id = Column(Integer)
    sort = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


# 人员信息
class UserInfo(base):
    __tablename__ = 'erp_ryxx'  # 表名
    id = Column(Integer, primary_key=True)
    erp_gsxx_id = Column(Integer, default=1003)
    username = Column(String(100))
    real_name = Column(String(100))
    mobile = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)


# 人员信息
class User(base):
    __tablename__ = 'erp_user'  # 表名
    id = Column(Integer, primary_key=True)
    erp_ckqx_id = Column(Integer)
    erp_bmqx_id = Column(Integer)
    full_name = Column(String(100))
    mobile = Column(String(100))
    status = Column(String(20), default="1")
    create_time = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime, default=datetime.now)