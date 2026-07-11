import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, func, 
                        ForeignKey)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship)

# From https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# Seems to be an SQLAlchemy thing but I don't understand the workings of it super well
class Base(DeclarativeBase):
    pass
# ---

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
    __tablename__ = "tickets"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(350))
    created_on = mapped_column(
        DateTime, server_default=func.now()
    )
    description = mapped_column(String(2000))
    # populates field "ticket" on Event instance
    # does not actually exist on ticket table
    # TODO: equal declaration on event object
    history = relationship(
        "Event", back_populates="ticket"
    )
    # "created by user id" is the actual table column
    created_by_user_id = mapped_column(
        Integer, ForeignKey("users.id")
    )
    # TODO: create this
    created_by_user = relationship(
        "User", back_populates="tickets_assigned"
    )
    # "assigned to user id" is the actual table column
    assigned_to_user_id = mapped_column(
        Integer, ForeignKey("users.id")
    )
    # TODO: create this
    assigned_to_user = relationship(
        "User", back_populates="tickets_created"
    )
    priority_id = mapped_column(
        Integer, ForeignKey("priority_levels.id")
    )
    # FIXME: this may break, not sure I got it correct
    priority = relationship("PriorityLevels")
    ticket_type_id = mapped_column(
        Integer, ForeignKey("ticket_types.id")
    )
    # TODO: change to datetime? timestamp?? time elapsed??
    estimated_time = mapped_column(
        String(350)
    )
    status_id = mapped_column(
        Integer, ForeignKey("ticket_statuses.id")
    )
    status = relationship("TicketStatus")


# -------------------------
#  Events
# -------------------------
class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  Priority Level
# -------------------------
class PriorityLevel(Base):
    __tablename__ = "priority_levels"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  Ticket Type
# -------------------------
class TicketType(Base):
    __tablename__ = "ticket_types"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  Ticket Status
# -------------------------
class TicketStatus(Base):
    __tablename__ = "ticket_statuses"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  Event Type
# -------------------------
class EventType(Base):
    __tablename__ = "event_types"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  Edited Field
# -------------------------
class EditedField(Base):
    __tablename__ = "edited_fields"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  User
# -------------------------
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

# -------------------------
#  User Role
# -------------------------
class UserRole(Base):
    __tablename__ = "user_roles"

    id: Mapped[int] = mapped_column(primary_key=True)

