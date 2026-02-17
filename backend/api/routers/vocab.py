from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vocab/random", response_model=schemas.VocabResponse)
def random_vocab(db: Session = Depends(get_db)):
    return crud.get_random_vocab(db)

@router.get("/vocab/jlpt/{level}", response_model=list[schemas.VocabResponse])
def vocab_by_level(level: int, db: Session = Depends(get_db)):
    return crud.get_vocab_by_jlpt(db, level)