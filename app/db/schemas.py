from pydantic import BaseModel


class MeasurementIn(BaseModel):
    name: str
    value: float
    type: str
    timestamp: int


class MeasurementDb(MeasurementIn):
    id: int


class Sensor(BaseModel):
    name: str
    block: str
    type: str
    status_code: int

    class Config:
        orm_mode = True


class SensorExtended(Sensor):
    measurements: list[MeasurementIn]


class ErrorIn(BaseModel):
    name: str
    status_code: int
    timestamp: int


class ErrorDb(ErrorIn):
    id: int
