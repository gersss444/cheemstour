from flask import Flask, request, jsonify
from entities.trip import Trip
from persistence.sqlalchemy_db import Base, engine


app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "API REST de Cheems Tour funcionando correctamente"})

@app.route('/trips', methods=['GET'])
def get_trips():
    trips = Trip.get()
    return jsonify(trips)

@app.route('/trips', methods=['POST'])
def create_trip():
    data = request.get_json()
    if not data or not all(key in data for key in ['name', 'city', 'country']):
        return jsonify({'error': 'Datos incompletos'}), 400
        
    result = Trip.create(
        name=data['name'],
        city=data['city'],
        country=data['country']
    )
    
    return jsonify(result), 201

if __name__ == '__main__':
    # Crear tablas antes de iniciar la aplicación
    Base.metadata.create_all(engine)
    print("Servidor iniciado en http://127.0.0.1:5000")
    app.run(debug=True)