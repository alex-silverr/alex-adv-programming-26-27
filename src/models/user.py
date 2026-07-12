import datetime
from typing import List
from sqlalchemy import (Integer, String, DateTime, Text, 
                        ForeignKey, Table, Column, func)
from sqlalchemy.orm import (DeclarativeBase, Mapped, 
                            mapped_column, relationship,
                            MappedAsDataclass, Session)
from sqlalchemy.ext.associationproxy import association_proxy
from ..database import Base, dbeng

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

    def serialize(self):
        with Session(dbeng) as session:
            j = {
                "display name": self.display_name,
                "full name": self.full_name,
                "e-mail": self.email,
                "github": self.github,
                "user role": self.r_role
            }
        return j