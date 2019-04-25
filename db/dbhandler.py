import  sqlalchemy
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String #区分大小写
from sqlalchemy.orm import sessionmaker

# 生成orm基类
base = declarative_base()

def query_brand(session,Cls,title):
    records = session.query(Cls).filter_by(title=title).all()
    if len(records) == 0:
        add_records(session,brand(title=title,status="1"))
        print("add band", title)

def add_records(session, objs):
   if isinstance(objs, list):
      session.add_all(objs)
   else:
      session.add(objs)
   session.commit()


def add_records(session, objs):
   if isinstance(objs, list):
      session.add_all(objs)
   else:
      session.add(objs)
   session.commit()


class brand(base):
    __tablename__ = 'erp_sppp'  # 表名
    id = Column(Integer, primary_key=True)
    title = Column(String(20))
    status = Column(String(20))

#创建连接
def create_session():
    #base.metadata.create_all(engine) #创建表结构
    engine = create_engine("mysql+pymysql://root:C9LRquJW@11.2.8.0:200/test", encoding='utf-8', echo=True)
    session_class=sessionmaker(bind=engine) ##创建与数据库的会话，class,不是实例
    session=session_class()   #生成session实例
    return session


#user_obj = brand(title="rr",status="1") #插入你要创建的数据对象，每执行一次都会新增一次数据。
#session.add(user_obj)  #把要创建的数据对象添加到这个session里
#session.commit() #提交，使前面修改的数据生效。



#query_brand(session,brand, '华为融合产品')