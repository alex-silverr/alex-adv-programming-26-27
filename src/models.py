from sqlalchemy.ext.delarative import declarative_base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

# From https://medium.com/@programersign/sqlalchemy-data-model-creation-333937341671
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
Base = declarative_base()
# ---

class Thing(Base):
    __tablename__= "things" 

    id: Mapped[int] = mapped_column(primary_key=True)
    thing: Mapped[str] = mapped_column(String(200))

    def __repr__(self):
        return "thing " + str(self.id) + " : " + self.thing