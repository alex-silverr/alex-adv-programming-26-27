from sqlalchemy.orm import Session
from src import dbeng
import src.connect as ct

def updateInfoEvent(id, args={}):
    """
    User UPDATE - aux:
    Update Event info for management reasons
    WARNING: should not be used in normal circumstances
    """
    id = int(id)
    event = ct.getEvent(id)

    with Session(dbeng) as session:
        if "user_id" in args: event.created_by = ct.getUser(args.get("user_id"))
        if "description" in args: event.description = args.get("description")

        session.commit()

    return event