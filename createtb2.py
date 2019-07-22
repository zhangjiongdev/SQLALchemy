#!/usr/bin/env python
# -*- coding:utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index
from sqlalchemy.orm import relationship
import os

Base = declarative_base()

# ##################### 单表示例 #########################
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

class Hosts(Base):
    __tablename__ = 'hosts'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True)
    ctime = Column(DateTime, default=datetime.datetime.now)

# ##################### 一对多示例 #########################
class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True)
    caption = Column(String(50), default='篮球')

class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)
    hobby_id = Column(Integer, ForeignKey("hobby.id"))
    # 与生成表结构无关，仅用于查询方便
    hobby = relationship("Hobby", backref='pers')

# ##################### 多对多示例 #########################
class Server2Group(Base):
    __tablename__ = 'server2group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    server_id = Column(Integer, ForeignKey('server.id'))
    group_id = Column(Integer, ForeignKey('group.id'))


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True, nullable=False)
    # 与生成表结构无关，仅用于查询方便
    servers = relationship('Server', secondary='server2group', backref='groups')

class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)

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
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
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
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.drop_all(engine)

if __name__ == '__main__':
    drop_db()
    init_db()
