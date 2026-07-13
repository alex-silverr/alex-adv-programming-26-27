from sqlalchemy.orm import Session
from src import dbeng
import src.connect as ct

def hardDeleteTicket(id):
    """
    Ticket DELETE - aux
    Ticket deletion function
    WARNING: should not be used in normal circumstances
    """
    id = int(id)
    ticket = ct.getTicket(id)

    with Session(dbeng) as session:
        session.delete(ticket)
        session.commit()
    return True