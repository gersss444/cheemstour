from flask import Flask
from entities.trip import Trip


app = Flask(__name__)

@app.route('/trips')
def trips():
    trips = Trip.get()
    return  trips

if __name__ == '__main__':
    app.run()