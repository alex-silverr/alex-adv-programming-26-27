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
    with Session(dbeng) as session:
        option = session.get(
            option_tables[table], id
        )
    return option

def optionGetByDesc(table, desc):
    """
    Aux Options - 
    Get option by description
    """
    with Session(dbeng) as session:
        option = session.scalars(
            select(option_tables[table])
            .where(
                option_tables[table].desc == desc
            ).order_by(
                option_tables[table].id
            )).first()
    return option

def optionCreateIfNotExist(table, desc):
    """
    Aux Options - 
    Create option if it doesn't exist
    """
    if not optionGetByDesc(table, desc):
        with Session(dbeng) as session:
            newoption = option_tables[table](desc=desc)
            session.add(newoption)
            session.commit()
        return newoption
    return True

def optionDelete(table, id):
    """
    Aux Options - 
    Delete option
    """
    option = optionGetById(table, id)
    with Session(dbeng) as session:
        session.delete(option)
        session.commit()
    return True
