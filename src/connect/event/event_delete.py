from sqlalchemy.orm import Session
from src import dbeng
import src.connect as ct

def hardDeleteEvent(id):
    """
    Event DELETE - aux
    Event deletion function
    WARNING: should not be used in normal circumstances
    """
    id = int(id)
    event = ct.getEvent(id)

    with Session(dbeng) as session:
        session.delete(event)
        session.commit()
    return True