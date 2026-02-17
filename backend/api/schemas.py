from pydantic import BaseModel

class VocabResponse(BaseModel):
    id: int
    kanji: str
    furigana: str | None
    english: str | None
    jlpt_level: int | None

    class Config:
        from_attributes = True