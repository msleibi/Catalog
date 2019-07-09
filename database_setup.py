import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Catigories(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
 
class Items(Base):
    __tablename__ = 'items'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Catigories)

#We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
       #Returns object data in easily serializeable format
       return {
           'name'         : self.name,
           'description'  : self.description,
           'id'         : self.id,
           }
 

engine = create_engine('sqlite:///catalogapp.db')
 

Base.metadata.create_all(engine)