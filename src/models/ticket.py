import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, Text, 
                        ForeignKey, Table, Column, func)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship,
                            MappedAsDataclass)
from sqlalchemy.ext.associationproxy import association_proxy
from ..database import Base


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
        "User", uselist=False, 
        foreign_keys=[created_by_user_id],
        lazy="selectin"
    )

    # Assigned To User: fk
    # - table goes through aux table {users_to_tickets}
    # - on db, only aux table exists
    # - assigned_to_user is the logical field
    assigned_to_user: Mapped[List["User"]] = relationship(
        secondary="users_to_tickets"
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
        "PriorityLevel", uselist=False, lazy="selectin"
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
        "TicketType", uselist=False, lazy="selectin"
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
        "TicketStatus", uselist=False, lazy="selectin"
    )
    status = association_proxy(
        "r_status", "desc"
    )

    # In retrospect I don't like the sub/supertickets idea

# aux table for users assigned to a ticket
users_to_tickets = Table(
    "users_to_tickets",
    Base.metadata,
    Column("ticket_id", ForeignKey("tickets.id")),
    Column("user_id", ForeignKey("users.id"))
)

def serialize(self):
        return {
                "title": self.title,
                "description": self.description,
                "created by": self.created_by_user.display_name,
                "priority": self.priority,
                "ticket type": self.ticket_type,
                "estimated_time": self.estimated_time,
                "status": self.status
            }