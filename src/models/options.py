import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, Text, 
                        ForeignKey, Table, Column, func)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship,
                            MappedAsDataclass)
from sqlalchemy.ext.associationproxy import association_proxy
from ..database import Base

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