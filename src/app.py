from flask import Flask, render_template, make_response, request, redirect
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

things = ["thing 1", "thing 2", "thing 3"]

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
        return things
    
    def post(self):
        """
        Barebones API: CREATE
        Creates new thing
        """
        thing = request.json.get("thing")
        if thing:
            things.append(thing)
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
            return things[index]
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
            thing = request.json.get("thing")
            if not thing:
                app.logger.error("No update value for instance given")
                return make_response(render_template("error_placeholder.html"))
            else:
                things[index] = thing
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
            things.pop(index)
            return redirect("/things")
        except Exception as e:
            app.logger.error(e)
            return make_response(render_template("error_placeholder.html"))


    
# class MakeThings(Resource):
#     """
#     Barebones API: CREATE
#     Page that creates a new "thing"
#     """
#     def post(self):
#         thing = request.json.get("thing")
#         if thing:
#             things.append(thing)
#         else:
#             app.logger.error("No thing to add")
#             return make_response(render_template("error_placeholder.html"))
#         return redirect("/things")

# class ShowThings(Resource):
#     """
#     Barebones API: READ
#     Page that shows "things" list
#     """
#     def get(self):
#         index = request.args.get('thing')
#         if index:
#             try:
#                 return things[int(index)]
#             except Exception as e:
#                 app.logger.error(e)
#                 return make_response(render_template("error_placeholder.html"))
#         return things
    
# class UpdateThings(Resource):
#     """
#     Barebones API: UPDATE
#     Page that updates a "thing"
#     """
#     def post(self):
#         which = request.json.get("which")
#         thing = request.json.get("thing")
#         if thing and which.isnumeric() and 0 <= int(which) <= len(things):
#             things[int(which)] = thing
#         else:
#             app.logger.error("No thing to change or no changed value to thing")
#             return make_response(render_template("error_placeholder.html"))
#         return redirect("/things")
    

# class RemoveThings(Resource):
#     """
#     Barebones API: DELETE
#     Page that removes a "thing"
#     """
#     def post(self):
#         which = request.json.get("which")
#         if which.isnumeric() and 0 <= int(which) <= len(things):
#             things.pop(int(which))
#         else:
#             app.logger.error("No thing to change or no changed value to thing")
#             return make_response(render_template("error_placeholder.html"))
#         return redirect("/things")
    



api.add_resource(Index, "/")
api.add_resource(Things, "/things", methods=['GET', 'POST'])
api.add_resource(Thing, "/thing/<int:index>", methods=['GET', 'PUT', 'DELETE'])
# api.add_resource(ShowThings, "/things")
# api.add_resource(MakeThings, "/newthing")
# api.add_resource(UpdateThings, "/changething")
# api.add_resource(RemoveThings, "/removething")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)