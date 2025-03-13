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

INSERT INTO users (first_name, last_name, email, contact_number, password) VALUES ('John', 'Smith', 'JohnSmith@gmail.com', '010 034 4455', 'password123');
INSERT INTO users (first_name, last_name, email, contact_number, password) VALUES ('Amy', 'Ryan', 'AmyRyan@outlook.com', '010 033 8274', 'snow755');
INSERT INTO users (first_name, last_name, email, contact_number, password) VALUES ('Callum', 'Brown', 'CallumBrown@icloud.com', '010 374 2174', 'football12');
INSERT INTO users (first_name, last_name, email, contact_number, password) VALUES ('Emma', 'Johnson', 'EmmaJohnson@gmail.com', '010 456 7890', 'secure123');
