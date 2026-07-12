from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src import Base, dbeng
from src.endpoints import (Index, ErrorLanding, 
                           ManageThing, ManageThings,
                           ManageTicket, ManageTickets,
                           ManageUser, ManageUsers,
                           ManageEvent, ManageEvents,
                           PriorityReadList, PriorityReadInstance,
                           TicketTypeReadList, TicketTypeReadInstance,
                           TicketStatusReadList, TicketStatusReadInstance,
                           EventTypeReadList, EventTypeReadInstance,
                           EditedFieldReadList, EditedFieldReadInstance,
                           UserRoleReadList, UserRoleReadInstance)

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

# READ endpoints for options
api.add_resource(PriorityReadList, "/priority", methods=['GET'])
api.add_resource(PriorityReadInstance, "/priority/<int:id>", methods=['GET'])
api.add_resource(TicketTypeReadList, "/ticket-type", methods=['GET'])
api.add_resource(TicketTypeReadInstance, "/ticket-type/<int:id>", methods=['GET'])
api.add_resource(TicketStatusReadList, "/ticket-status", methods=['GET'])
api.add_resource(TicketStatusReadInstance, "/ticket-status/<int:id>", methods=['GET'])
api.add_resource(EventTypeReadList, "/event-type", methods=['GET'])
api.add_resource(EventTypeReadInstance, "/event-type/<int:id>", methods=['GET'])
api.add_resource(EditedFieldReadList, "/edited-field", methods=['GET'])
api.add_resource(EditedFieldReadInstance, "/edited-field/<int:id>", methods=['GET'])
api.add_resource(UserRoleReadList, "/role", methods=['GET'])
api.add_resource(UserRoleReadInstance, "/role/<int:id>", methods=['GET'])

# Test CRUD endpoints for "Thing"
api.add_resource(ManageThings, "/things", methods=['GET', 'POST'])
api.add_resource(ManageThing, "/thing/<int:index>", methods=['GET', 'PUT', 'DELETE'])



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)