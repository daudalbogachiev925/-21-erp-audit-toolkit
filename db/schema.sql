CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL,
    name TEXT,
    kind TEXT CHECK (kind IN ('active','passive','ap'))
);

CREATE TABLE documents (
    id BIGSERIAL PRIMARY KEY,
    doc_type TEXT,
    doc_date DATE,
    amount NUMERIC(15,2),
    status TEXT DEFAULT 'posted',
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE postings (
    id BIGSERIAL PRIMARY KEY,
    document_id BIGINT REFERENCES documents(id) ON DELETE CASCADE,
    debit_account TEXT REFERENCES accounts(code),
    credit_account TEXT REFERENCES accounts(code),
    amount NUMERIC(15,2) NOT NULL CHECK (amount > 0),
    description TEXT,
    created TIMESTAMP DEFAULT NOW()
);

CREATE TABLE balances (
    id BIGSERIAL PRIMARY KEY,
    account_code TEXT REFERENCES accounts(code),
    period DATE,
    debit NUMERIC(15,2),
    credit NUMERIC(15,2),
    UNIQUE(account_code, period)
);

CREATE INDEX idx_postings_doc ON postings(document_id);
CREATE INDEX idx_postings_debit ON postings(debit_account);
CREATE INDEX idx_postings_credit ON postings(credit_account);
