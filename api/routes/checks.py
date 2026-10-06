from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

CHECKS = {
    'balance': 'checks/balance_check.sql',
    'duplicates': 'checks/duplicates.sql',
    'anomalies': 'checks/anomalies.sql',
    'unbalanced': 'checks/unbalanced.sql',
    'unused': 'checks/unused_accounts.sql',
    'reconciliation': 'checks/reconciliation.sql'
}

@router.get("/{name}")
def run_check(name: str, db: Session = Depends(get_session)):
    if name not in CHECKS:
        return {"error": f"Неизвестная проверка: {name}",
                "available": list(CHECKS.keys())}
    rows = db.execute(text(open(CHECKS[name]).read())).fetchall()
    return {"check": name, "rows": [dict(r._mapping) for r in rows]}
