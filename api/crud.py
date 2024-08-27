from sqlmodel import Session, select
from models import Item, ItemCreate


def create_item(db: Session, item: ItemCreate):
    db_item = Item.from_orm(item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_item(db: Session, item_id: int):
    return db.get(Item, item_id)


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.exec(select(Item).offset(skip).limit(limit)).all()


def update_item(db: Session, item_id: int, item: ItemCreate):
    db_item = db.get(Item, item_id)
    if db_item:
        item_data = item.dict(exclude_unset=True)
        for key, value in item_data.items():
            setattr(db_item, key, value)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.get(Item, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
