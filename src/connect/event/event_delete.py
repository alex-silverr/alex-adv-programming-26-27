from sqlalchemy import select
from sqlalchemy.orm import Session
from src import dbeng
from src.connect import getEvent

def hardDeleteEvent(id):
    """
    Event DELETE - aux
    Event deletion function
    WARNING: should not be used in normal circumstances
    """
    id = int(id)
    event = getEvent(id)

    with Session(dbeng) as session:
        session.delete(event)
        session.commit()
    return True