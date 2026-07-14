from sqlalchemy.orm import Session
from src import dbeng
from flask import current_app
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
        ticket.assigned_to_user = []
        session.delete(ticket)
        session.commit()
    return True