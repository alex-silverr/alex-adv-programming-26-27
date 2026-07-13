from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from src import dbeng
from src.models import Event

def searchEvent(args={}):
    """
    Event READ - aux:
    Searches Events with optional query arguments
    """
    events_query = select(Event)

    # Search by ticket
    if "ticket_id" in args:
        events_query = events_query.where(
            Event.ticket.id == args.get("ticket_id")
        )

    # Search by creating user
    if "created_by" in args:
        events_query = events_query.where(
            Event.created_by.id == args.get("created_by_id")
        )

    # Search by created after date
    if "created_start" in args:
        events_query = events_query.where(
            Event.created_on > args.get("created_start")
        )

    # Search by created before date
    if "created_end" in args:
        events_query = events_query.where(
            Event.created_on < args.get("created_end")
        )

    events_query = events_query.order_by(desc(Event.registered_on))

    with Session(dbeng) as session:
        events = session.scalars(events_query).all()
    return events

def getAllEvents():
    """
    Event READ - aux:
    Get unique event by id
    """
    with Session(dbeng) as session:
        events = session.scalars(
            select(Event)
            .order_by(Event.id)
        ).all()
    return events

def getEvent(id=None):
    """
    Event READ - aux:
    Get unique event by id
    """
    if not id:
        raise ValueError("No id provided!")
    
    id = int(id)
    with Session(dbeng) as session:
        event = session.get(
            Event, id
        )
    
    if not event:
        raise ValueError("Incorrect event identification!")
    return event