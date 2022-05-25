'''
-*- encoding: utf-8 -*-
@文件: database.py
@时间: 2022/04/18 21:12:31
@作者: 咸鱼型233
@说明: 创建 SQLAlchemy 
'''
# Import the SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# sqlite 数据库 url
SQLALCHEMY_DATABASE_URL = "sqlite:///./ViteLearningBackend.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# 创建 SQLAlchemy 引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建SessionLocal 类
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建一个 Base 类, 后面继承这个类来创建每个数据库的 ORM Model
Base = declarative_base()
