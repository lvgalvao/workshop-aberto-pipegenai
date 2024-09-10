CREATE TABLE IF NOT EXISTS vendas (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            data TIMESTAMP NOT NULL,
            valor NUMERIC NOT NULL,
            quantidade INTEGER NOT NULL,
            produto VARCHAR(50) NOT NULL
)