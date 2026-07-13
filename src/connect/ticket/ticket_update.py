from sqlalchemy.orm import Session
from src import dbeng
from src.connect import getTicket, getUser
from src.models import (User, PriorityLevel,
                    TicketType, TicketStatus) 

def updateInfoTicket(id, args={}):
    """
    Ticket UPDATE - aux:
    Update Ticket info: title, description or priority
    """
    id = int(id)
    ticket = getTicket(id)

    with Session(dbeng) as session:
        if "title" in args: ticket.title = args.get("title")
        if "description" in args: ticket.description = args.get("description")
        if "priority_id" in args:
            priority = session.get(PriorityLevel, args.get("priority_id"))
            if not priority: raise ValueError("Could not update ticket: invalid priority level.")
            ticket.r_priority = priority

        session.commit()
    return ticket

# if I've set up relationships properly, this is unecessary
# def addHistoryTicket(id, args={}):
#     """
#     Ticket UPDATE - aux:
#     Assign Event to Ticket history
#     """
#     pass

def assignToUserTicket(id, args={}):
    """
    Ticket UPDATE - aux:
    Assign User to Ticket
    """
    id = int(id)
    ticket = getTicket(id)
    if "assign_user_id" in args:
        user = getUser(args.get("assign_user_id"))
    else:
        raise ValueError("User to assign ticket to not given")
    
    with Session(dbeng) as session:
        ticket.assigned_to_user.append(user)
        session.commit()
    return ticket

def updateEstimatedTimeTicket(id, args={}):
    """
    Ticket UPDATE - aux:
    Change Ticket's estimated time to completion
    """
    id = int(id)
    ticket = getTicket(id)

    with Session(dbeng) as session:
        if "estimated_time" in args: ticket.estimated_time = args.get("estimated_time")
        session.commit()
    return ticket

def changeStatusTicket(id, args={}):
    """
    Ticket UPDATE - aux:
    Change Ticket status
    """
    id = int(id)
    ticket = getTicket(id)

    with Session(dbeng) as session:
        if "status_id" in args:
            status = session.get(TicketStatus, args.get("status_id"))
            if not status: raise ValueError("Could not update ticket: invalid status.")
            ticket.r_status = status
        session.commit()
    return ticket

def generalUpdateTicket(id, args={}):
    """
    Ticket UPDATE - aux:
    Management/general Ticket update function
    """
    id = int(id)
    ticket = getTicket(id)


    with Session(dbeng) as session:
        # Fetching relationed objects and checking validity

        if "user_id" in args:
            user = session.get(User, args.get("user_id"))
            if not user: raise ValueError("Could not update ticket: invalid user.")
            ticket.created_by_user = user

        if "priority_id" in args:
            priority = session.get(PriorityLevel, args.get("priority_id"))
            if not priority: raise ValueError("Could not update ticket: invalid priority level.")
            ticket.r_priority = priority

        if "ticket_type_id" in args:
            ticket_type = session.get(TicketType, args.get("ticket_type_id"))
            if not ticket_type: raise ValueError("Could not update ticket: invalid ticket type.")
            ticket.r_ticket_type = ticket_type

        if "status_id" in args:
            status = session.get(TicketStatus, args.get("status_id"))
            if not status: raise ValueError("Could not update ticket: invalid status.")
            ticket.r_status = status

        # Updating direct values
        if "title" in args: ticket.title = args.get("title")
        if "description" in args: ticket.description = args.get("description")
        if "estimated_time" in args: ticket.estimated_time = args.get("estimated_time")

        session.commit()
    return ticket