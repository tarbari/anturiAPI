from sqlalchemy import Column, Integer, String
from .init_db import Base


# TODO: Sensors class might need a separate id column
class Sensors(Base):
    __tablename__ = 'sensors'
    name = Column(String, primary_key=True, index=True)
    block = Column(String, nullable=False)
    sensor_type = Column(Integer, nullable=False)
    status_code = Column(Integer, nullable=False)


class Error(Base):
    __tablename__ = 'error'
    id = Column(Integer, primary_key=True, index=True)
    sensor = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    timestamp = Column(Integer, nullable=False)


class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True, index=True)
    sensor = Column(String, nullable=False)
    sensor_type = Column(Integer, nullable=False)
    timestamp = Column(Integer, nullable=False)
