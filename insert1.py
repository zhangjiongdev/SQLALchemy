#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship


import os

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    age = Column(Integer, default=18)
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)
    extra = Column(Text, nullable=True)

    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'extra'),
    )




env_dist = os.environ
pwdstr = env_dist['mysqldbpwd'].replace("\\","")
engine = create_engine(
"mysql+pymysql://root:"+ pwdstr +"@30.0.2.101:3306/t1?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）——永不回收-1
)

Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
session = Session()

# ############# 执行ORM操作 #############
obj1 = Users(name="alex1")
session.add(obj1)

# 提交事务
session.commit()
# 关闭session
session.close()


