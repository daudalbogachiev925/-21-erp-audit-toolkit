INSERT INTO accounts (code, name, kind) VALUES
('50','Касса','active'),
('51','Расчётный счёт','active'),
('60','Поставщики','ap'),
('62','Покупатели','ap'),
('90.1','Выручка','passive'),
('99','Прибыли и убытки','ap');

INSERT INTO documents (doc_type, doc_date, amount) VALUES
('Реализация','2024-01-10',50000),
('Оплата','2024-01-15',50000),
('Закупка','2024-01-20',30000),
('Зарплата','2024-01-31',120000);

INSERT INTO postings (document_id, debit_account, credit_account, amount) VALUES
(1,'62','90.1',50000),
(2,'51','62',50000),
(3,'60','51',30000),
(4,'99','51',120000);
