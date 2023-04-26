import sqlalchemy.exc
import time
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas import Sensor, Error, SensorExtended
from app.db.models import Sensors, Errors, Measurements


def crud_read_all_sensors(db: Session):
    result = db.query(Sensors).all()
    if len(result) == 0:
        raise HTTPException(detail='Sensors not found in database', status_code=status.HTTP_404_NOT_FOUND)
    return result


def crud_read_sensor_by_name(db: Session, name: str, start_time: int, end_time: int):
    sensor = db.query(Sensors).filter(Sensors.name == name).first()
    if sensor is None:
        raise HTTPException(detail=f'Sensor not found. Name: {name}', status_code=status.HTTP_404_NOT_FOUND)
    if (start_time == 0) and (end_time == 0):
        measurements = db.query(Measurements) \
            .order_by(Measurements.timestamp.desc()) \
            .filter(Measurements.name == name) \
            .limit(10) \
            .all()
    else:
        measurements = db.query(Measurements) \
            .order_by(Measurements.timestamp.desc()) \
            .filter(Measurements.name == name,
                    Measurements.timestamp >= start_time,
                    Measurements.timestamp <= end_time) \
            .all()
    result = SensorExtended(**sensor.__dict__, measurements=measurements)
    return result


def crud_read_sensors_by_block(db: Session, block: str):
    result = db.query(Sensors).filter(Sensors.block == block).all()
    if len(result) == 0:
        raise HTTPException(detail='Block not found', status_code=status.HTTP_404_NOT_FOUND)
    for sensor in result:
        measurements = db.query(Measurements) \
            .order_by(Measurements.timestamp.desc()) \
            .filter(Measurements.name == sensor.name) \
            .limit(1) \
            .all()
        sensor.measurements = measurements
    return result


def crud_read_sensor_by_status(db: Session, status_code: int):
    result = db.query(Sensors).filter(Sensors.status_code == status_code).all()
    if len(result) == 0:
        raise HTTPException(detail=f'Sensors with status_code not found: {status_code}',
                            status_code=status.HTTP_404_NOT_FOUND)
    return result


# TODO: This could use input validation to keep naming conventions consistent
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
        raise HTTPException(detail='Sensor not found', status_code=status.HTTP_404_NOT_FOUND)
    db_sensor.status_code = status_code
    error = Error(name=name, status_code=status_code, timestamp=timestamp)
    db_error = Errors(**error.dict())
    db.add(db_error)
    db.commit()
    db.refresh(db_sensor)
    db.refresh(db_error)
    return db_sensor


def crud_update_sensor_block(db: Session, name: str, block: str):
    db_sensor = db.query(Sensors).filter(Sensors.name == name).first()
    if db_sensor is None:
        raise HTTPException(detail='Sensor not found', status_code=status.HTTP_404_NOT_FOUND)
    db_sensor.block = block
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


# TODO: Remove this before returning
def crud_destroy_sensor(db: Session, name: str):
    result = db.query(Sensors).filter(Sensors.name == name).delete()
    db.commit()
    return result
