from sqlalchemy import Column, Integer, String
from database import Base

class Vocabulary(Base):
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    kanji = Column(String, nullable=False)
    furigana = Column(String)
    english = Column(String)
    jlpt_level = Column(Integer)