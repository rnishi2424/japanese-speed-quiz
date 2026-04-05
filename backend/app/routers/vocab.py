from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
import app.crud, app.schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vocab/random", response_model=app.schemas.VocabResponse)
def random_vocab(db: Session = Depends(get_db)):
    return app.crud.get_random_vocab(db)

@router.get("/vocab/jlpt/{level}", response_model=list[app.schemas.VocabResponse])
def vocab_by_level(level: int, db: Session = Depends(get_db)):
    return app.crud.get_vocab_by_jlpt(db, level)