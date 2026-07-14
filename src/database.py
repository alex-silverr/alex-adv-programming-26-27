import datetime
from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from src.settings import SQLALCHEMY_DATABASE_URL
import src.connect as ct

# -------------------------------
# Base from https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
class Base(DeclarativeBase):
    pass
# --------------------------------


dbeng = create_engine(SQLALCHEMY_DATABASE_URL) 

startup_options ={
    "ticket_type": ["Error", "Issue", "Vulnerability", 
                    "Feature", "Requirements"],

    "priority_level": ["Urgent", "High Priority", 
                       "Medium Priority", "Low Priority", 
                       "Background Task"],

    "ticket_status": ["New", "Approved", "Assigned", 
                      "In Progress", "On Hold", 
                      "Resolved", "Removed"],

    "event_type": ["Ticket Detail Changed", 
                   "User Assigned", 
                   "Estimated Duration Changed", 
                   "Status Changed", 
                   "History Entry Added"],

    "user_role": ["Developer", "Analyst", 
                  "Manager", "Designer", "Owner", 
                  "QA", "Tester"]
}

for table, options in startup_options.items():
    for option in options:
        ct.optionCreateIfNotExist(table, option)
