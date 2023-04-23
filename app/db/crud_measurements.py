# TODO: Needs work
from sqlalchemy.orm import Session
from app.db.schemas import MeasurementIn


def crud_create_measurement(db: Session, measurement: MeasurementIn):
    return 0


def crud_delete_measurement(db: Session, name: str, timestamp: int):
    return 0
