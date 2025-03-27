from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar la conexión a la base de datos
DATABASE_URL = "postgresql://postgres.hgxoohrxwgugotqpafiz:A54C4jofR5OPgS25@aws-0-us-west-1.pooler.supabase.com:6543/postgres"
engine = create_engine(DATABASE_URL)

# Crear una clase base para las entidades
Base = declarative_base()

# Crear una clase para el creador de sesiones
Session = sessionmaker(bind=engine)

# Función para obtener una sesión
def get_session():
    return Session() 