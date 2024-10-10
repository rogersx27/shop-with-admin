from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException
import uuid


def create_instance(db: Session, model, schema):
    db_instance = model(id=str(uuid.uuid4()), **schema.dict())
    db.add(db_instance)
    db.commit()
    db.refresh(db_instance)
    return db_instance


def create_instance_only(db: Session, model, schema):
    db_instance = model(id=str(uuid.uuid4()), **schema.dict())
    return db_instance


def get_all_instances(db: Session, model):
    return db.query(model).all()


def get_instance_by_id(db: Session, model, instance_id: str | uuid.UUID):
    instance = db.query(model).filter(model.id == instance_id).first()
    if not instance:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return instance


def update_instance(db: Session, model, instance_id: str | uuid.UUID, update_schema) -> object:
    instance = db.query(model).filter(model.id == instance_id).first()
    if not instance:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")

    for key, value in update_schema.dict().items():
        setattr(instance, key, value)
    db.commit()
    db.refresh(instance)
    return instance


def delete_instance(db: Session, model, instance_id: uuid.UUID | str) -> dict[str, str]:
    instance = db.query(model).filter(model.id == instance_id).first()
    if not instance:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")

    db.delete(instance)
    db.commit()
    return {"detail": f"{model.__name__} deleted successfully"}
