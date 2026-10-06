from fastapi import FastAPI
from routes import documents, postings, checks, reports

app = FastAPI(title="ERP Audit Toolkit")

app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(postings.router, prefix="/postings", tags=["postings"])
app.include_router(checks.router, prefix="/checks", tags=["checks"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
