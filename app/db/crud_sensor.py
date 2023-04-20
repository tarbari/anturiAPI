import sqlalchemy.exc
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.schemas import Sensor
from app.db.models import Sensors, Measurements


def read_all_sensors(db: Session):
    return db.query(Sensors).all()


# TODO: Add 10 most recent measurements to the return value
#    - Also need a query parameter for the time window of the measurements to show
def read_sensor_by_name(db: Session, name: str):
    return db.query(Sensors).filter(Sensors.name == name).first()


# TODO: Add latest measurement for each sensor to the return value
def read_sensors_by_block(db: Session, block: str):
    return db.query(Sensors).filter(Sensors.block == block).all()


def read_sensors_by_status(db: Session, status_code: int):
    return db.query(Sensors).filter(Sensors.status_code == status_code).all()


def create_sensor(db: Session, sensor: Sensor):
    try:
        db_sensor = Sensors(**sensor.dict())
        db.add(db_sensor)
        db.commit()
        db.refresh(db_sensor)
        return db_sensor
    except sqlalchemy.exc.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))


def update_sensor_status(db: Session, name: str, status_code: int):
    db_sensor = db.query(Sensors).filter(Sensors.name == name).first()
    db_sensor.status_code = status_code
    # TODO: Check if this actually works o.o
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


def update_sensor_block(db: Session, name: str, block: str):
    db_sensor = db.query(Sensors).filter(Sensors.name == name).first()
    db_sensor.block = block
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


# TODO: Remove this before returning
def destroy_sensor(db: Session, name: str):
    result = db.query(Sensors).filter(Sensors.name == name).delete()
    db.commit()
    return result
