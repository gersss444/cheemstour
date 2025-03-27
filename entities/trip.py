from sqlalchemy import Column, Integer, String
from persistence.sqlalchemy_db import Base, get_session

class Trip(Base):
    __tablename__ = 'trips'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    country = Column(String)
    
    def __init__(self, name=None, city=None, country=None):
        self.name = name
        self.city = city
        self.country = country
    
    @classmethod
    def get(cls):
        try:
            session = get_session()
            trips = session.query(cls).all()
            
            result = []
            for trip in trips:
                result.append({
                    'id': trip.id,
                    'name': trip.name,
                    'city': trip.city,
                    'country': trip.country
                })
                
            return result
        except Exception as ex:
            return str(ex)
        finally:
            session.close()
            
    @classmethod
    def create(cls, name, city, country):
        try:
            session = get_session()
            trip = cls(name=name, city=city, country=country)
            session.add(trip)
            session.commit()
            
            return {
                'id': trip.id,
                'name': trip.name,
                'city': trip.city,
                'country': trip.country
            }
        except Exception as ex:
            session.rollback()
            return str(ex)
        finally:
            session.close()