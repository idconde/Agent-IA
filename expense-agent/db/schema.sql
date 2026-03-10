CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    date TIMESTAMP,
    amount NUMERIC,
    category TEXT,
    description TEXT
);