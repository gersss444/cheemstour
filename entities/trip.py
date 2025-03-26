


from mysql.connector import Error
from persistance.db import get_connection

class Trip:
    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country


@classmethod
def get(cls):
    try:
        conection = get_connection()
        cursor = conection.cursor(dictionary=True) 
        cursor.execute('SELECT id, name, city, country FROM trips')
        return cursor.fetchall()
    except Error as ex:
        return str(ex)
    finally:   
        cursor.close()
        conection.close()