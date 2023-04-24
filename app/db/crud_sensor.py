import sqlalchemy.exc
import time
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas import Sensor, ErrorIn
from app.db.models import Sensors, Error


def crud_read_all_sensors(db: Session):
    return db.query(Sensors).all()


# TODO: Add 10 most recent measurements to the return value
#    - Also need a query parameter for the time window of the measurements to show
def crud_read_sensor_by_name(db: Session, name: str, start_time: int, end_time: int):
    return db.query(Sensors).filter(Sensors.name == name).first()


# TODO: Add latest measurement for each sensor to the return value
def crud_read_sensors_by_block(db: Session, block: str):
    result = db.query(Sensors).filter(Sensors.block == block).all()
    if len(result) == 0:
        raise HTTPException(detail='Block not found (╯°□°)╯︵ ┻━┻', status_code=status.HTTP_404_NOT_FOUND)
    return result


def crud_read_sensor_by_status(db: Session, status_code: int):
    return db.query(Sensors).filter(Sensors.status_code == status_code).all()


# This could use input validation to keep naming conventions consistent
def crud_create_sensor(db: Session, sensor: Sensor):
    try:
        db_sensor = Sensors(**sensor.dict())
        db.add(db_sensor)
        db.commit()
        db.refresh(db_sensor)
        return db_sensor
    except sqlalchemy.exc.IntegrityError as e:
        raise HTTPException(detail=str(e), status_code=400)


def crud_update_sensor_status(db: Session, name: str, status_code: int):
    timestamp = int(time.time())
    db_sensor = db.query(Sensors).filter(Sensors.name == name).first()
    if db_sensor is None:
        raise HTTPException(detail='Sensor not found ¯\_(ツ)_/¯', status_code=status.HTTP_404_NOT_FOUND)
    db_sensor.status_code = status_code
    # Not proud of this next bit >_>
    error = ErrorIn(name=name, status_code=status_code, timestamp=timestamp)
    db_error = Error(**error.dict())
    print(error)
    db.add(db_error)
    db.commit()
    db.refresh(db_sensor)
    db.refresh(db_error)
    return db_sensor


def crud_update_sensor_block(db: Session, name: str, block: str):
    db_sensor = db.query(Sensors).filter(Sensors.name == name).first()
    db_sensor.block = block
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


# TODO: Remove this before returning
def crud_destroy_sensor(db: Session, name: str):
    result = db.query(Sensors).filter(Sensors.name == name).delete()
    db.commit()
    return result
