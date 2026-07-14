from sqlalchemy.orm import Session
from src import dbeng
from src.models import User
import src.connect as ct

def makeUser(args={}):
    """
    User CREATE - aux:
    Creates a new User from passed arguments
    """

    # Checks presence of mandatory arguments
    for arg in ["display_name", "full_name", "email",
                "role_id"]:
        if arg not in args:
            raise ValueError(f"Could not create user: {arg} missing")
        
        
    # Fills for optional arguments
    if not args.get("github"): args["github"] = ""

    # Fetching relationed objects and checking validity
    role = ct.optionGetById("user_role", args.get("role_id"))
    if not role: raise ValueError("Could not create user: invalid user role")

    # Create user
    with Session(dbeng) as session:
        newuser = User(
            display_name = args.get("display_name"),
            full_name = args.get("full_name"),
            email = args.get("email"),
            github = args.get("github"),
            r_role = role
        )
        session.add(newuser)
        session.commit()
    
    return newuser


