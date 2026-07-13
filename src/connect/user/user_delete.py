from sqlalchemy.orm import Session
from src import dbeng
from src.connect import getTicket

def deleteUser(id):
    """
    User DELETE - aux
    Removes an user
    """
    id = int(id)
    user = getTicket(id)

    with Session(dbeng) as session:
        session.delete(user)
        session.commit()
    return True