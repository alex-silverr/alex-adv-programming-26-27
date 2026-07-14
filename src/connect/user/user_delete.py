from sqlalchemy.orm import Session
from src import dbeng
import src.connect as ct

def deleteUser(id):
    """
    User DELETE - aux
    Removes an user
    """
    id = int(id)
    user = ct.getUser(id)

    with Session(dbeng) as session:
        session.delete(user)
        session.commit()
    return True