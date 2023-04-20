from pydantic import BaseModel


# TODO: If you add separate id column to Sensors class, add it here too
class Sensor(BaseModel):
    name: str
    block: str
    sensor_type: int
    status_code: int

    class Config:
        orm_mode = True


class MeasurementIn(BaseModel):
    sensor: str
    sensor_type: int
    timestamp: int


class MeasurementDb(MeasurementIn):
    id: int


class ErrorIn(BaseModel):
    sensor: str
    status_code: int
    timestamp: int


class ErrorDb(ErrorIn):
    id: int
