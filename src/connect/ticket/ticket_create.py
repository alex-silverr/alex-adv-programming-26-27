from sqlalchemy.orm import Session
from src import dbeng
from src.models import (Ticket, User, PriorityLevel,
                    TicketType, TicketStatus) 

def makeTicket(args={}):
    """
    Ticket CREATE - aux:
    Makes a Ticket from passed arguments
    """

    # Checks presence of mandatory arguments
    for arg in ["title", "user_id", "priority_id", 
                "ticket_type_id"]:
        if arg not in args:
            raise ValueError(f"Could not create ticket: {arg} missing.")
        
    # Fills for optoional arguments
    if not args.get("description"): args["description"] = ""
    if not args.get("estimated_time"): args["estimated_time"] = "Unknown"

    with Session(dbeng) as session:
        # Fetching relationed objects and checking validity
        
        user = session.get(User, args.get("user_id"))
        if not user: raise ValueError("Could not create ticket: invalid user.")

        priority = session.get(PriorityLevel, args.get("priority_id"))
        if not priority: raise ValueError("Could not create ticket: invalid priority level.")

        ticket_type = session.get(TicketType, args.get("ticket_type_id"))
        if not ticket_type: raise ValueError("Could not create ticket: invalid ticket type.")

        status = session.get(TicketStatus, 1)

        # Create ticket
        newticket = Ticket(
            title = args.get("title"),
            description = args.get("description"),
            # TODO: history?
            created_by_user = user,
            # TODO: assigned to?
            r_priority = priority,
            r_ticket_type = ticket_type,
            estimated_time = args.get("estimated_time"),
            r_status = status
        )
        session.add(newticket)
        session.commit()

    return newticket