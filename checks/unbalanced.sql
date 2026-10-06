-- Документы, где Дт ≠ Кт по сумме
SELECT document_id,
       SUM(CASE WHEN debit_account IS NOT NULL THEN amount ELSE 0 END) AS dr,
       SUM(CASE WHEN credit_account IS NOT NULL THEN amount ELSE 0 END) AS cr
FROM postings
GROUP BY document_id
HAVING SUM(CASE WHEN debit_account IS NOT NULL THEN amount ELSE 0 END)
     <> SUM(CASE WHEN credit_account IS NOT NULL THEN amount ELSE 0 END);
