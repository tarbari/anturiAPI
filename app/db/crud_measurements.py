import time
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db.schemas import MeasurementIn
from app.db.models import Measurements, Sensors


def crud_create_measurement(db: Session, measurement: MeasurementIn):
    new_measurement = Measurements(**measurement.dict())
    # Making sure the sensor exists
    sensor = db.query(Sensors).filter(Sensors.name == measurement.name).first()
    if sensor is None:
        raise HTTPException(detail=f'Sensor not found. Name: {measurement.name}', status_code=status.HTTP_404_NOT_FOUND)
    new_measurement.timestamp = int(time.time())
    new_measurement.value = round(measurement.value, 1)
    db.add(new_measurement)
    db.commit()


def crud_delete_measurement(db: Session, name: str, timestamp: int):
    db.query(Measurements).filter(Measurements.name == name, Measurements.timestamp == timestamp).delete()
    db.commit()
