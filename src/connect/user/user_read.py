from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from src import dbeng
from src.models import User

def searchUser(args={}):
    """
    User READ - aux:
    Searches Users with optional query arguments
    """
    users_query = select(User)

    # Search by display name
    if "display_name" in args:
        users_query = users_query.where(
            User.display_name == args.get("display_name")
        )

    # Search by email
    if "email" in args:
        users_query = users_query.where(
            User.email == args.get("email")
        )

    # Search by role
    if "role" in args:
        users_query = users_query.where(
            User.role == args.get("role")
        )

    users_query = users_query.order_by(desc(User.registered_on))

    with Session(dbeng) as session:
        users = session.scalars(users_query).all()
    return users

def getAllUsers():
    """
    User READ - aux:
    Get unique user by id
    """
    with Session(dbeng) as session:
        users = session.scalars(
            select(User)
            .order_by(User.id)
        ).all()
    return users

def getUser(id=None):
    """
    User READ - aux:
    Get unique user by id
    """
    if not id:
        raise ValueError("No id provided!")
    
    id = int(id)
    with Session(dbeng) as session:
        user = session.get(
            User, id
        )
    
    if not user:
        raise ValueError("Incorrect user identification!")
    return user