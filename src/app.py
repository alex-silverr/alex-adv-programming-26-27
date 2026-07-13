from flask import (Flask)
from flask_restful import Api
from src import Base, dbeng
from src.endpoints import *

app = Flask(__name__)
api = Api(app)

Base.metadata.create_all(dbeng)


# Basic or utility endpoints
api.add_resource(Index, "/")
api.add_resource(ErrorLanding, "/oops")

# Ticket Endpoints
api.add_resource(CreateTicket, "/tickets/new", methods=['POST'])
api.add_resource(ReadTicketList, "/tickets", methods=['GET'])
api.add_resource(ReadTicketInstance, "/tickets/<int:id>", methods=['GET'])
api.add_resource(UpdateTicketUpdateInfo, "/tickets/change-info/<int:id>", methods=['POST'])
# api.add_resource(UpdateTicketAddHistoryEvent, "/tickets/add-history/<int:id>", methods=['POST'])
api.add_resource(UpdateTicketAssignUser, "/tickets/add-user/<int:id>", methods=['POST'])
api.add_resource(UpdateTicketEstimatedTime, "/tickets/change-time/<int:id>", methods=['POST'])
api.add_resource(UpdateTicketChangeStatus, "/tickets/change-status/<int:id>", methods=['POST'])

# User Endpoints
api.add_resource(CreateUser, "/users/new", methods=['POST'])
api.add_resource(ReadUserList, "/users", methods=['GET'])
api.add_resource(ReadUserInstance, "/users/<int:id>", methods=['GET'])
api.add_resource(UpdateUserInfo, "/users/change-info/<int:id>", methods=['POST'])
api.add_resource(DeleteUser, "/users/delete/<int:id>", methods=['DELETE'])

# Event Endpoints
api.add_resource(CreateHistoryEvent, "/event/history/new", methods=['POST'])
api.add_resource(ReadEventList, "/event", methods=['GET'])
api.add_resource(ReadEventInstance, "/event/<int:id>", methods=['GET'])

# Basic/Management CRUD endpoints for Ticket objects
api.add_resource(ManageTickets, "/manage-tickets", methods=['GET', 'POST'])
api.add_resource(ManageTicket, "/manage-ticket/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# Basic/Management CRUD endpoints for User objects
api.add_resource(ManageUsers, "/manage-users", methods=['GET', 'POST'])
api.add_resource(ManageUser, "/manage-user/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# Basic/Management CRUD endpoints for Event objects
api.add_resource(ManageEvents, "/manage-events", methods=['GET', 'POST'])
api.add_resource(ManageEvent, "/manage-event/<int:id>", methods=['GET', 'PATCH', 'DELETE'])

# READ endpoints for options
api.add_resource(PriorityReadList, "/priority", methods=['GET'])
api.add_resource(PriorityReadInstance, "/priority/<int:id>", methods=['GET'])
api.add_resource(TicketTypeReadList, "/ticket-type", methods=['GET'])
api.add_resource(TicketTypeReadInstance, "/ticket-type/<int:id>", methods=['GET'])
api.add_resource(TicketStatusReadList, "/ticket-status", methods=['GET'])
api.add_resource(TicketStatusReadInstance, "/ticket-status/<int:id>", methods=['GET'])
api.add_resource(EventTypeReadList, "/event-type", methods=['GET'])
api.add_resource(EventTypeReadInstance, "/event-type/<int:id>", methods=['GET'])
api.add_resource(UserRoleReadList, "/role", methods=['GET'])
api.add_resource(UserRoleReadInstance, "/role/<int:id>", methods=['GET'])

# Test CRUD endpoints for "Thing"
api.add_resource(ManageThings, "/things", methods=['GET', 'POST'])
api.add_resource(ManageThing, "/thing/<int:index>", methods=['GET', 'PUT', 'DELETE'])



if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)