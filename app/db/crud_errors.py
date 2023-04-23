# TODO: Needs work
from sqlalchemy.orm import Session
from app.db.schemas import ErrorIn


def crud_get_all_errors(db: Session, error: ErrorIn):
    return 0


def crud_get_error_by_name(db: Session, name: str):
    return 0
