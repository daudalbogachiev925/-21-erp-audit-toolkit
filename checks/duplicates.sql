-- Дубли документов по типу+дате+сумме
SELECT doc_type, doc_date, amount, COUNT(*) AS n
FROM documents
GROUP BY doc_type, doc_date, amount
HAVING COUNT(*) > 1;
