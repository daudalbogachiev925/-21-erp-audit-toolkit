-- Счета без движения
SELECT a.code, a.name FROM accounts a
WHERE NOT EXISTS (
    SELECT 1 FROM postings p
    WHERE p.debit_account = a.code OR p.credit_account = a.code
);
