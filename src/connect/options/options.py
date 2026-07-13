from sqlalchemy import select
from sqlalchemy.orm import Session
from src import dbeng
from src.models import (TicketType, PriorityLevel, TicketStatus,
                        EventType, UserRole)

option_tables = {
    "ticket_type": TicketType,
    "priority_level": PriorityLevel,
    "ticket_status": TicketStatus,
    "event_type": EventType,
    "user_role": UserRole
}

def optionGetAll(table):
    """
    Aux Options - 
    Get all options
    """
    with Session(dbeng) as session:
        options = session.scalars(
            select(option_tables[table])
            .order_by(
                option_tables[table].id
            )
        ).all()
    return options

def optionGetById(table, id):
    """
    Aux Options - 
    Get option by id
    """
    pass

def optionGetByDesc(table, desc):
    """
    Aux Options - 
    Get option by description
    """
    pass

def optionCreateIfNotExist(table, desc):
    """
    Aux Options - 
    Create option if it doesn't exist
    """
    pass

def optionDelete(table, desc):
    """
    Aux Options - 
    Delete option
    """
    pass
