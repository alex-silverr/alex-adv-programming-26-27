from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from .database import Base, Thing
from .models.ticket import Ticket
from .models.event import Event
from .models.user import User
from .models.options import *
from .settings import SQLALCHEMY_DATABASE_URL

app = Flask(__name__)
api = Api(app)

dbeng = create_engine(SQLALCHEMY_DATABASE_URL) 
Base.metadata.create_all(dbeng)
# thing1 = Thing(thing="thing 1")
# thing2 = Thing(thing="thing 2")
# thing3 = Thing(thing="thing 3")

# with Session(dbeng) as session:
#     session.add_all([thing1, thing2, thing3])
#     session.commit()


# -------------------------
#  Thing and Things
# -------------------------

class Index(Resource):
    """
    Default/placeholder index
    """
    def get(self):
        return make_response(render_template("home.html"))
    
class Things(Resource):
    """
    Barebones API: list resource
    """

    def get(self):
        """
        Barebones API: list READ
        Returns all things
        """
        with Session(dbeng) as session:
            things = session.scalars(
                select(Thing)
                .order_by(Thing.id)
            ).all()
        return jsonify([t.serialize() for t in things])
    
    def post(self):
        """
        Barebones API: CREATE
        Creates new thing
        """
        thing = request.json.get("thing")
        if thing:
            with Session(dbeng) as session:
                newthing = Thing(thing=thing)
                session.add(newthing)
                session.commit()
        else:
            app.logger.error("No thing to add")
            return make_response(render_template("error_placeholder.html"))
        return redirect("/things")
    
class Thing(Resource):
    """
    Barebones API: instance resource
    """

    def get(self, index=None):
        """
        Barebones API: instance READ
        Returns a thing
        """
        try:
            index = int(index)
            with Session(dbeng) as session:
                thing = session.get(
                    Thing, index
                )
            return jsonify(thing.serialize())
        except Exception as e:
            app.logger.error(e)
            return make_response(render_template("error_placeholder.html"))

    def put(self, index=None):
        """
        Barebones API: UPDATE
        Changes content of a thing
        """
        try:
            index = int(index)
            thingv = request.json.get("thing")
            if not thingv:
                app.logger.error("No update value for instance given")
                return make_response(render_template("error_placeholder.html"))
            else:
                with Session(dbeng) as session:
                    thing = session.get(
                        Thing, index
                    )
                    thing.thing = thingv
                    session.commit()
                return redirect("/things")
        except Exception as e:
            app.logger.error(e)
            return make_response(render_template("error_placeholder.html"))
        
    def delete(self, index=None):
        """
        Barebones API: DELETE
        Removes a thing
        """
        try:
            index = int(index)
            with Session(dbeng) as session:
                thing = session.get(
                    Thing, index
                )
                session.delete(thing)
                session.commit()
            return redirect("/things")
        except Exception as e:
            app.logger.error(e)
            return make_response(render_template("error_placeholder.html"))
        


api.add_resource(Index, "/")
api.add_resource(Things, "/things", methods=['GET', 'POST'])
api.add_resource(Thing, "/thing/<int:index>", methods=['GET', 'PUT', 'DELETE'])




if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)