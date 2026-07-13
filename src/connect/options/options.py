from sqlalchemy.orm import Session
from src import dbeng
from src.models import (TicketType, PriorityLevel, TicketStatus,
                        EventType, UserRole)

def optionGetAll(table):
    """
    Aux Options - 
    Get all options
    """
    pass

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
