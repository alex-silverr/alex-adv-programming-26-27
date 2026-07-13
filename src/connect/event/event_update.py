from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from src import dbeng
from src.connect import getEvent, getUser
from src.models import Event

def updateInfoEvent(id, args={}):
    """
    User UPDATE - aux:
    Update Event info for management reasons
    WARNING: should not be used in normal circumstances
    """
    id = int(id)
    event = getEvent(id)

    with Session(dbeng) as session:
        if "user_id" in args: event.created_by = getUser(args.get("user_id"))
        if "description" in args: event.description = args.get("description")

        session.commit()

    return event