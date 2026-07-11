import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, Text, 
                        ForeignKey, func)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship,
                            MappedAsDataclass)
from sqlalchemy.ext.associationproxy import association_proxy

# -------------------------------
# Base from https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
class Base(DeclarativeBase):
    pass
# --------------------------------

class Thing(Base):
    __tablename__= "things" 

    id: Mapped[int] = mapped_column(primary_key=True)
    thing: Mapped[str] = mapped_column(String(200))

    def __repr__(self):
        return "thing " + str(self.id) + " : " + self.thing
    
    def serialize(self):
        return {"thing" : self.thing}
    

# -------------------------
#  Tickets
# -------------------------
class Ticket(Base):
    """
    MODEL: Ticket
    TABLE: tickets
    """
    __tablename__ = "tickets"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)
    
    # Title: str(350)
    title = mapped_column(String(350))
    
    # Created On: datetime, date on creation
    created_on = mapped_column(
        DateTime, server_default=func.now()
    )

    # Description: text
    description = mapped_column(Text)
    
    # History: Event list
    # - backpopulates field {ticket} on Event
    # - does not actually create a column
    # - can be empty: create empty list as default
    history = relationship(
        "Event", back_populates="ticket"
    )
    # history = relationship(
    #     "Event", back_populates="ticket",
    #     default_factory=list
    # )

    # Created By User: fk
    # - table fk field mapped to {users.id}
    # - backpopulates field {tickets_assigned} on User
    # - created_by_user_id exists on db
    # - created_by_user is the logical field
    created_by_user_id = mapped_column(
        Integer, ForeignKey("users.id")
    )
    created_by_user = relationship(
        "User", uselist=False
    )

    # Assigned To User: fk
    # TODO: for now only maps to one user
    # TODO: change to many-to-many in the future
    # - table fk field mapped to {users.id}
    # - backpopulates field {tickets_created}
    # - assigned_to_user_id exists on db
    # - assigned_to_user is the logical field
    assigned_to_user_id = mapped_column(
        Integer, ForeignKey("users.id"), nullable=True
    )
    assigned_to_user = relationship(
        "User", uselist=False
    )

    # Priority: fk
    # - table fk field mapped to {priority_levels.id}
    # - doesn't backpopulate a field
    # - priority_id is the db field
    # - r_priority is the logical field
    # - priority is the direct logical field by "desc"
    priority_id = mapped_column(
        Integer, ForeignKey("priority_levels.id")
    )
    r_priority = relationship(
        "PriorityLevels", uselist=False
    )
    priority = association_proxy("r_priority", "desc")
    
    # Ticket type: fk
    # - table fk mapped to {ticket_types.id}
    # - doesn't backpopulate to a field
    # - ticket_type_id is the db field
    # - r_ticket_type is the logical field
    # - ticket_type is the direct logical field by "desc"
    ticket_type_id = mapped_column(
        Integer, ForeignKey("ticket_types.id")
    )
    r_ticket_type = relationship(
        "TicketType", uselist=False
    )
    ticket_type = association_proxy(
        "r_ticket_type", "desc"
    )

    # Estimated Time: ???
    # - string for now
    # - need a better format
    # - datetime? some sort of timestamp?
    # - I want the time delta represented in text
    estimated_time = mapped_column(
        String(350)
    )

    # Status: fk
    # - table fk mapped to {ticket_statuses.id}
    # - doesn't backpopulate to a field
    # - status_id is the db field
    # - r_status is the logical field
    # - status is the direct logical field by "desc"
    status_id = mapped_column(
        Integer, ForeignKey("ticket_statuses.id")
    )
    r_status = relationship(
        "TicketStatus", uselist=False
    )
    status = association_proxy(
        "r_status", "desc"
    )

    # - TODO: subtickets: fk
    # - TODO: superticket: fk


# -------------------------
#  Events
# -------------------------
class Event(Base):
    """
    MODEL: Event
    TABLE: events
    """
    __tablename__ = "events"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Created By: fk
    # - table fk mapped to {users.id}
    # - does not backpopulate to a field
    # - created_by_id is the db field
    # - created_by is the logical field
    created_by_id = mapped_column(
        Integer, ForeignKey("users.id")
    )
    created_by = relationship(
        "User", uselist=False
    )
    
    # Ticket: fk
    # - table fk mapped to {tickets.id}
    # - backpopulates field {history} on Ticket
    # - {history} is a list field of Events
    # - ticket_id is the db field
    # - ticket is the logical field
    ticket_id = mapped_column(
        Integer, ForeignKey("tickets.id")
    )
    ticket = relationship(
        "Ticket", back_populates="history"
    )

    # Created On: datetime, date on creation
    created_on = mapped_column(
        DateTime, server_default=func.now()
    )

    # Event Type: fk
    # - table fk mapped to {event_types.id}
    # - does not backpopulate to a field
    # - event_type_id is the db field
    # - r_event_type is the logical field
    # - event_type is the direct logical field by "desc"
    event_type_id = mapped_column(
        Integer, ForeignKey("event_types.id")
    )
    r_event_type = relationship(
        "EventType", uselist=False
    )
    event_type = association_proxy(
        "r_event_type", "desc"
    )

    # Description: text
    # - only when event type is "History item"
    description = mapped_column(Text, nullable=True)
    
    # TODO: Edited Field: fk
    # - for now only text fields
    # - until I figure out how to do new/former properly
    # TODO: Former Value: ?
    # TODO: New Value: ?

# -------------------------
#  Priority Level
# -------------------------
class PriorityLevel(Base):
    """
    MODEL: PriorityLevel
    TABLE: priority_levels
    """
    __tablename__ = "priority_levels"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

# -------------------------
#  Ticket Type
# -------------------------
class TicketType(Base):
    """
    MODEL: TicketType
    TALBE: ticket_types
    """
    __tablename__ = "ticket_types"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

# -------------------------
#  Ticket Status
# -------------------------
class TicketStatus(Base):
    """
    MODEL: TicketStatus
    TABLE: ticket_statuses
    """
    __tablename__ = "ticket_statuses"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

# -------------------------
#  Event Type
# -------------------------
class EventType(Base):
    """
    MODEL: EventType
    TABLE: event_types
    """
    __tablename__ = "event_types"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

# -------------------------
#  Edited Field
# -------------------------
class EditedField(Base):
    """
    MODEL: EditedField
    TABLE: edited_fields
    """
    __tablename__ = "edited_fields"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

# -------------------------
#  User
# -------------------------
class User(Base):
    """
    MODEL: User
    TABLE: users
    """
    __tablename__ = "users"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Display Name: str(200)
    display_name = mapped_column(String(200))

    # Full Name: str(350)
    full_name = mapped_column(String(350))

    # Registered On: datetime, date on creation
    registered_on = mapped_column(
        DateTime, server_default=func.now()
    )

    # E-mail: str(200)
    email = mapped_column(String(200))

    # GitHub: str(200)
    github = mapped_column(String(200))
    
    # Role: fk
    # - table fk mapped to {user_roles.id}
    # - does not backpopulate to a field
    # - role_id is the db field
    # - r_role is the logical field
    # - role is the direct logical field by "desc"
    role_id = mapped_column(
        Integer, ForeignKey("user_roles.id")
    )
    r_role = relationship(
        "UserRole", uselist=False
    )
    role = association_proxy("r_role", "desc")


# -------------------------
#  User Role
# -------------------------
class UserRole(Base):
    """
    MODEL: UserRole
    TABLE: user_roles
    """
    __tablename__ = "user_roles"

    # ID: int, pk, auto generated
    id = mapped_column(Integer, primary_key=True)

    # Desc: str(200)
    desc = mapped_column(String(200))

