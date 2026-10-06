-- Проверка: сумма дебетовых = сумма кредитных (в целом по базе)
SELECT
    (SELECT COALESCE(SUM(amount),0) FROM postings) AS total_debit,
    (SELECT COALESCE(SUM(amount),0) FROM postings) AS total_credit;
