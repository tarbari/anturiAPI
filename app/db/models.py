from sqlalchemy import Column, Integer, String, Float
from .initialize_database import Base


class Sensors(Base):
    __tablename__ = 'sensors'
    name = Column(String, primary_key=True, index=True)
    block = Column(String, nullable=False)
    type = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)


class Errors(Base):
    __tablename__ = 'errors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status_code = Column(Integer, nullable=False)
    timestamp = Column(Integer, nullable=False)


class Measurements(Base):
    __tablename__ = 'measurements'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(Integer, nullable=False)
