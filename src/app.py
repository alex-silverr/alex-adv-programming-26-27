from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    """
    This is a default/placeholder page to test if I understood how Flask works.
    """
    return render_template("home.html")

# This is from the Flask tutorial given in class
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')