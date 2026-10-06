-- Сверка оборотов и остатков
SELECT a.code, a.name,
       COALESCE(SUM(p.amount) FILTER (WHERE p.debit_account = a.code),0) AS turn_dr,
       COALESCE(SUM(p.amount) FILTER (WHERE p.credit_account = a.code),0) AS turn_cr,
       COALESCE(MAX(b.debit),0) - COALESCE(MAX(b.credit),0) AS balance
FROM accounts a
LEFT JOIN postings p ON p.debit_account = a.code OR p.credit_account = a.code
LEFT JOIN balances b ON b.account_code = a.code
GROUP BY a.code
ORDER BY a.code;
