# import flask library
from flask import Flask, request, jsonify

# Creating Flask Application
app = Flask(__name__)

# Adding a decorater "Demo route"
@app.route("/")   # '/' default root

# GET route -> request data from a specified resource
# POST -> Create a resource
# PUT -> Update a resource
# DELETE -> Delete a resource




# GET route
@app.route("/get-user/<user_id>")
def get_user(user_id = 12345):
    user_data = {
        "user_id": user_id,
        "name": "Yogesh Pal",
        "email": "parmar****pal@gmail.com"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data ), 200



# POST route
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

# Further this API can be tested for POST request on Postman app.




# Creating a root
def home():
    return "Home"

# Running Flask application 
if __name__ == "__main__":
    app.run(debug = True)
