import datetime
from sqlalchemy import (Integer, DateTime, Text, 
                        ForeignKey, func)
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.ext.associationproxy import association_proxy
from src import Base

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
        "User", uselist=False, lazy="selectin"
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
        "Ticket", back_populates="history", lazy="selectin"
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
        "EventType", uselist=False, lazy="selectin"
    )
    event_type = association_proxy(
        "r_event_type", "desc"
    )

    # Description: text
    # - only when event type is "History item"
    description = mapped_column(Text, nullable=True)
    
    # Edits can be registered in description honestly

    def serialize(self):
        return {
                "created on": self.created_on,
                "created by": self.created_by.display_name or None,
                "ticket": self.ticket.title,
                "event type": self.event_type,
                "description": self.description
            }