#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:supery

import os
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)          # 主键
    name = Column(String(32), index=True, nullable=False)   # 添加索引，不能为空
    email = Column(String(32), unique=True)
    ctime = Column(DateTime, default=datetime.datetime.now)
    # datetime.datetime.now不能加括号，加括号默认值就是第一次插入时间
    # extra = Column(Text, nullable=True)
    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),    # 联合唯一索引
        Index('ix_id_name', 'name', 'email'),                   # 普通索引
    )
    _table_arhs__ = {
        'mysql_engine': 'InnoDb',                   # 设置表引擎
        'mysql_charset': 'utf8'                     # 设置表字符集
    }

class qrcode(Base):
    __tablename__ = 'tb_qrcode'
    idx = Column(Integer, primary_key=True)          # 主键
    qrcodestr = Column(String(32), index=True, nullable=False)   # 添加索引，不能为空
    ctime = Column(DateTime, default=datetime.datetime.now)
    _table_arhs__ = {
        'mysql_engine': 'InnoDb',                   # 设置表引擎
        'mysql_charset': 'utf8'                     # 设置表字符集
    }

def init_db():
    """
    根据类创建数据库表
    :return:
    """
    env_dist = os.environ
    pwdstr = env_dist['mysqldbpwd'].replace("\\","")
    engine = create_engine(
    "mysql+pymysql://root:"+ pwdstr +"@30.0.2.101:3306/t1?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）——永不回收-1
    )
    Base.metadata.create_all(engine)

def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    env_dist = os.environ
    pwdstr = env_dist['mysqldbpwd'].replace("\\","")
    engine = create_engine(
    "mysql+pymysql://root:"+ pwdstr +"@30.0.2.101:3306/t1?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）——永不回收-1
    )
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    # 初始化数据库，先删除再创建
    drop_db()
    init_db()