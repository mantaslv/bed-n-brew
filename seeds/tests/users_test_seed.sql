DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    contact_number VARCHAR(20),
    password VARCHAR(255)
    );

INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Bilbo', 'Baggins', '0789 123 8765', 'bilbob59@hobbitmail.org', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');
INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Mario', 'Mario', '0800 100 400', 'mario@warioland.com', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');
