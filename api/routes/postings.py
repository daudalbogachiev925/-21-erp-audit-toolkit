from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PIn(BaseModel):
    document_id: int
    debit_account: str
    credit_account: str
    amount: float
    description: str | None = None

@router.post("/")
def create(data: PIn, db: Session = Depends(get_session)):
    if data.amount <= 0:
        raise HTTPException(400, "Сумма должна быть > 0")
    row = db.execute(text("""
        INSERT INTO postings (document_id, debit_account, credit_account, amount, description)
        VALUES (:document_id,:debit_account,:credit_account,:amount,:description)
        RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/document/{doc_id}")
def by_document(doc_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT * FROM postings WHERE document_id=:i
    """), {"i": doc_id}).fetchall()]
