'''
-*- encoding: utf-8 -*-
@文件: models.py
@时间: 2022/04/19 08:45:45
@作者: 咸鱼型233
@说明: 创建 database models
'''
from tokenize import Double
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, FLOAT
from sqlalchemy.orm import relationship

from .database import Base


class Admin(Base):
    __tablename__ = "admin"

    uid = Column(Integer, primary_key=True, index=True)
    password = Column(String)

class Good(Base):
    __tablename__ = "Good"

    GoodID = Column(Integer, primary_key=True, index=True)
    GoodName = Column(String)
    GoodPrice = Column(FLOAT)
