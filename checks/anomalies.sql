-- Аномальные проводки: сумма > 3σ от среднего по счёту
WITH stats AS (
    SELECT debit_account AS acc, AVG(amount) AS m, STDDEV(amount) AS s
    FROM postings GROUP BY debit_account
)
SELECT p.id, p.document_id, p.debit_account, p.amount,
       s.m AS avg_amount, s.s AS stddev
FROM postings p
JOIN stats s ON s.acc = p.debit_account
WHERE p.amount > s.m + 3 * s.s;
