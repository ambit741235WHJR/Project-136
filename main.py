# Importing Flask
from flask import Flask, request, jsonify

# Importing the data from the data.py file
from data import data

# Creating an App for Flask
app = Flask(__name__)

# Creating a route for the root path
@app.route('/')
def index():
    return jsonify({
        'data': data,
        'message': 'success'
    }), 200

# Creating a route for the /planet path
@app.route('/stars', methods=['GET'])
def planet():
    # Getting the star name from the URL
    star_name = request.args.get('name')
    # Creating a variable to store the planet data
    star_data = next(star for star in data if star['name'] == star_name)
    # Returning the planet data
    return jsonify({
        'data': star_data,
        'message': 'success'
    }), 200

# Calling the app
if __name__ == '__main__':
    app.run(debug=True)