from persistence.db import get_connection
from mysql.connector import Error

class Trip:
    def __init__(self, id, name, city, country):
        self.id = id
        self.name = name
        self.city = city
        self.country = country

    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, name, city, country FROM trips')
            trips = cursor.fetchall()
            return trips
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def create(cls, name, city, country):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "INSERT INTO trips (name, city, country) VALUES (%s, %s, %s)",
                (name, city, country)
            )
            connection.commit()
            return {"message": "Viaje creado exitosamente"}
        except Error as ex:
            return {"error": str(ex)}
        finally:
            cursor.close()
            connection.close()
