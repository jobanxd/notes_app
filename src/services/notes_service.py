from sqlalchemy.orm import Session
from models.notes import Notes
from schema.notes import NoteCreate

def get_notes(db: Session):
    return db.query(Notes).all()

def create_notes(db: Session, notes_data: NoteCreate):
    note = Notes(**notes_data)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

def get_notes_by_id(db: Session, id: int):
    pass

