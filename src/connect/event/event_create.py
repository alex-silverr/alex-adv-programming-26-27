from sqlalchemy import select
from sqlalchemy.orm import Session
from src import dbeng
from src.connect import getUser
from src.models import (Event, EventType, User, Ticket, TicketStatus) 

def makeEvent(args={}):
    """
    Event CREATE - aux:
    Makes a Event from passed arguments and created description.
    """

    # Checks presence of mandatory arguments
    for arg in ["ticket_id", "user_id", "event_type"]:
        if arg not in args:
            raise ValueError(f"Could not create event: {arg} missing.")
        

    # Creates description based on event type
    # Unless the event is "History entry added"
    # In which case the description should be provided beforehand
    if not args.get("description"):
        match args.get("event_type"):
            case "Ticket Detail Changed":
                args["description"] = f"Ticket details edited"

            case "User Assigned":
                args["description"] = f"Ticket assigned to {
                    getUser(args.get("assign_user_id")).display_name
                }"

            case "Estimated Duration Changed":
                args["description"] = f"Estimated duration changed to {
                    args.get("estimated_time")
                }."
                
            case "Status Changed":
                with Session(dbeng) as session:
                    args["description"] = f"Ticket status changed to {
                        session.get(TicketStatus, args.get("status_id")).desc
                    }"

            case "History Entry Added":
                raise ValueError("An event history must have a description.")
            
            case _:
                raise ValueError("Could not create event: event type does not \
                                match any known event type. Has a new type been \
                                added?")
            
    with Session(dbeng) as session:
        # Fetching relationed objects and checking validity
        user = session.get(User, args.get("user_id"))
        if not user: raise ValueError("Could not create event: invalid user.")

        ticket = session.get(Ticket, args.get("ticket_id"))
        if not ticket: raise ValueError("Could not create event: invalid ticket.")

        event_type = session.scalars(
            select(EventType).where(
                EventType.desc == args.get("event_type")
            )
        ).first()
        if not event_type: raise ValueError("Could not create event: invalid event type.")

        # Create event
        newevent = Event(
            description = args.get("description"),
            created_by = user,
            ticket = ticket,
            r_event_type = event_type

        )
        session.add(newevent)
        session.commit()

    return newevent