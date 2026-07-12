from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from .database import Base, Thing, dbeng
from .models.ticket import Ticket
from .models.event import Event
from .models.user import User
from .models.options import (PriorityLevel, TicketType, TicketStatus,
                             EventType, EditedField, UserRole)
from .endpoints.testthing import ManageThing, ManageThings
from .endpoints.manageticket import ManageTicket, ManageTickets
from .endpoints.manageuser import ManageUser, ManageUsers
from .endpoints.manageevent import ManageEvent, ManageEvents
from .endpoints.utils import Index, ErrorLanding
from .settings import SQLALCHEMY_DATABASE_URL

app = Flask(__name__)
api = Api(app)

Base.metadata.create_all(dbeng)


# Basic or utility endpoints
api.add_resource(Index, "/")
api.add_resource(ErrorLanding, "/oops")

# Basic CRUD endpoints for Ticket objects
api.add_resource(ManageTickets, "/tickets", methods=['GET', 'POST'])
api.add_resource(ManageTicket, "/ticket/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# Basic CRUD endpoints for User objects
api.add_resource(ManageUsers, "/users", methods=['GET', 'POST'])
api.add_resource(ManageUser, "/user/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# Basic CRUD endpoints for Event objects
api.add_resource(ManageEvents, "/events", methods=['GET', 'POST'])
api.add_resource(ManageEvent, "/event/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# Test CRUD endpoints for "Thing"
api.add_resource(ManageThings, "/things", methods=['GET', 'POST'])
api.add_resource(ManageThing, "/thing/<int:index>", methods=['GET', 'PUT', 'DELETE'])



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)