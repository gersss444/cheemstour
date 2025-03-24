import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            