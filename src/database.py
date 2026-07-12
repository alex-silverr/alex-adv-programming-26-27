import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, Text, 
                        ForeignKey, Table, Column, func,
                        create_engine)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship,
                            MappedAsDataclass)
from sqlalchemy.ext.associationproxy import association_proxy
from .settings import SQLALCHEMY_DATABASE_URL

# -------------------------------
# Base from https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
class Base(DeclarativeBase):
    pass
# --------------------------------


dbeng = create_engine(SQLALCHEMY_DATABASE_URL) 

class Thing(Base):
    __tablename__= "things" 

    id: Mapped[int] = mapped_column(primary_key=True)
    thing: Mapped[str] = mapped_column(String(200))

    def __repr__(self):
        return "thing " + str(self.id) + " : " + self.thing
    
    def serialize(self):
        return {"thing" : self.thing}
    