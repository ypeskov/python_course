from sqlalchemy import Column, Integer, String, DateTime

from .database import db


class Password(db.Model):
    id = Column(Integer, primary_key=True)
    resource_name = Column(String(100), unique=False, nullable=True)
    url = Column(String, nullable=False, default='')
    login = Column(String, nullable=False, default='')
    password = Column(String, nullable=False, default='')
    comment = Column(String, nullable=True)
