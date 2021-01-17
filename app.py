"""This is an example of a simple API."""

from flask import Flask, request
app = Flask(__name__)

# http://127.0.0.1:5000/home base url
@app.route('/home')
def index():
    return 'Hello Flask'

# http://127.0.0.1:5000/users/2 base url
@app.route('/users/<user_id>', methods= ['GET', 'POST', 'PUT', 'DELETE'])  # url adresi dinamik hale geldi <> bunun ile
def parameter(user_id):
    if request.method == 'GET':  # GET = READ
        return 'GET method'

    elif request.method == 'POST':  # POST = CREATE
        data = request.form
        return data

    elif request.method == 'PUT':  # PUT = UPDATE

        return 'PUT method'

    elif request.method == 'DELETE':  # DELETE = DELETE
        return 'DELETE method'

    else:
        return 'Not a Method'

app.run()
# app.run(host='localhost', port=81) böyle de calistirilabilir