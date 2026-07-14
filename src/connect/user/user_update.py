from sqlalchemy.orm import Session
from flask import current_app

from src import dbeng
import src.connect as ct

def updateInfoUser(id, args={}):
    """
    User UPDATE - aux:
    Update User info: display name, full name, e-mail, github, role
    """
    id = int(id)
    user = ct.getUser(id)

    with Session(dbeng) as session:
        if "display_name" in args: user.display_name = args.get("display_name")
        if "full_name" in args: user.full_name = args.get("full_name")
        if "email" in args: user.email = args.get("email")
        if "github" in args: user.github = args.get("github")
        if "role_id" in args:
            role = ct.optionGetById("user_role", args.get("role_id"))
            if not role: raise ValueError("Could not update user: invalid role")
            role.r_role = role

        session.merge(user)
        session.commit()
    return user