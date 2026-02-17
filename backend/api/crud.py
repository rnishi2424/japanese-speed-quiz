from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Vocabulary

def get_random_vocab(db: Session):
    return db.query(Vocabulary).order_by(func.random()).first()

def get_vocab_by_jlpt(db: Session, level: int):
    return db.query(Vocabulary).filter(
        Vocabulary.jlpt_level == level
    ).all()