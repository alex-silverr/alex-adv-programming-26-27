from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from src import dbeng
from src.models import Ticket

# CREATE: Create new
#  UPDATE: Edit info (Title, Description, Priority)
#  UPDATE: Add history item
#  UPDATE: Assign to user
#  UPDATE: Change estimated time
#  UPDATE: Change status ("DELETE": Removed status)

def searchTicket(args={}):
    """
    Ticket READ - aux:
    Searches Tickets with optional query arguments
    """
    tickets_query = select(Ticket)
    
    # Search by similar title
    if "title" in args:
        tickets_query = tickets_query.where(
            Ticket.title.like(args.get("title"))
        )

    # Searc by created after date
    if "created_start" in args:
        tickets_query = tickets_query.where(
            Ticket.created_on > args.get("created_start")
        )

    # Search by created before date
    if "created_end" in args:
        tickets_query = tickets_query.where(
            Ticket.created_on < args.get("created_end")
        )
    
    # Search by created by user
    if "created_by" in args:
        tickets_query = tickets_query.where(
            Ticket.created_by_user.id == args.get("created_by")
        )
    
    # TODO: assigned_to

    # Search by priority level
    if "priority" in args:
        tickets_query = tickets_query.where(
            Ticket.priority == args.get("priority")
        )

    # Search by ticket type
    if "ticket_type" in args:
        tickets_query = tickets_query.where(
            Ticket.ticket_type == args.get("ticket_type")
        )

    # Search by ticket status
    if "status" in args:
        tickets_query = tickets_query.where(
            Ticket.status == args.get("status")
        )

    
    tickets_query = tickets_query.order_by(desc(Ticket.created_on))

    with Session(dbeng) as session:
        tickets = session.scalars(tickets_query).all()
    return tickets

def getAllTickets():
    """
    Ticket READ - aux:
    Get all tickets
    """
    with Session(dbeng) as session:
        tickets = session.scalars(
            select(Ticket)
            .order_by(Ticket.id)
        ).all()
    return tickets

def getTicket(id=None):
    """
    Ticket READ - aux:
    Get unique ticket by id
    """
    if not id:
        raise ValueError("No id provided!")
    
    id = int(id)
    with Session(dbeng) as session:
        ticket = session.get(
            Ticket, id
        )
    
    if not ticket:
        raise ValueError("Incorrect ticket identification!")
    return ticket
