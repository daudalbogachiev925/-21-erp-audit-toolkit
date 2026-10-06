from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class DIn(BaseModel):
    doc_type: str
    doc_date: date
    amount: float

@router.post("/")
def create(data: DIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO documents (doc_type, doc_date, amount)
        VALUES (:doc_type,:doc_date,:amount) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM documents ORDER BY doc_date DESC LIMIT 500
    """)).fetchall()]
