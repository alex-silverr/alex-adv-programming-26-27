from sqlalchemy.orm import Session
from src import dbeng
from flask import current_app
import src.connect as ct
from src.models import Event

def makeEvent(args={}):
    """
    Event CREATE - aux:
    Makes a Event from passed arguments and created description.
    """

    current_app.logger.debug("ping")

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
                    ct.getUser(args.get("assign_user_id")).display_name
                }"

            case "Estimated Duration Changed":
                args["description"] = f"Estimated duration changed to {
                    args.get("estimated_time")
                }."
                
            case "Status Changed":
                args["description"] = f"Ticket status changed to {
                    ct.optionGetById("ticket_status", args.get("status_id")).desc
                }"

            case "History Entry Added":
                raise ValueError("An event history must have a description.")
            
            case _:
                raise ValueError("Could not create event: event type does not \
                                match any known event type. Has a new type been \
                                added?")
            
    current_app.logger.debug("pong")
    # Fetching relationed objects and checking validity
    user = ct.getUser(args.get("user_id"))
    if not user: raise ValueError("Could not create event: invalid user.")

    current_app.logger.debug("ting")
    ticket = ct.getTicket(args.get("ticket_id"))
    if not ticket: raise ValueError("Could not create event: invalid ticket.")

    event_type = ct.optionGetByDesc("event_type", args.get("event_type"))
    if not event_type: raise ValueError("Could not create event: invalid event type.")

    current_app.logger.debug("tang")
    # Create event
    with Session(dbeng) as session:
        current_app.logger.debug("bing")
        newevent = Event(
            description = args.get("description"),
            created_by = user,
            ticket = ticket,
            r_event_type = event_type

        )
        current_app.logger.debug("bong")
        session.add(newevent)
        session.commit()

    return newevent