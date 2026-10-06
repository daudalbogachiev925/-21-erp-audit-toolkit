from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/turnover/{account_code}")
def turnover(account_code: str, db: Session = Depends(get_session)):
    row = db.execute(text("""
        SELECT
            (SELECT COALESCE(SUM(amount),0) FROM postings WHERE debit_account=:c) AS turn_debit,
            (SELECT COALESCE(SUM(amount),0) FROM postings WHERE credit_account=:c) AS turn_credit
    """), {"c": account_code}).fetchone()
    return dict(row._mapping)

@router.get("/trial-balance")
def trial_balance(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT a.code, a.name,
            COALESCE(SUM(p.amount) FILTER (WHERE p.debit_account = a.code),0) AS dr,
            COALESCE(SUM(p.amount) FILTER (WHERE p.credit_account = a.code),0) AS cr,
            COALESCE(SUM(p.amount) FILTER (WHERE p.debit_account = a.code),0)
              - COALESCE(SUM(p.amount) FILTER (WHERE p.credit_account = a.code),0) AS balance
        FROM accounts a
        LEFT JOIN postings p ON p.debit_account = a.code OR p.credit_account = a.code
        GROUP BY a.code, a.name
        ORDER BY a.code
    """)).fetchall()]
