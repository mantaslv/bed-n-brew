DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS hosts;
DROP SEQUENCE IF EXISTS hosts_id_seq;

CREATE SEQUENCE IF NOT EXISTS hosts_id_seq;
CREATE TABLE hosts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    contact_number VARCHAR(20),
    email VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    property_name VARCHAR(255),
    location VARCHAR(255),
    beds INTEGER,
    property_type VARCHAR(255),
    price_per_night FLOAT,
    description TEXT,
    image_url TEXT,
    rating SMALLINT,
    availability TEXT,
    booked_dates TEXT,
    host_id INTEGER,
    CONSTRAINT fk_host FOREIGN KEY (host_id) REFERENCES hosts(id) ON DELETE CASCADE
);

INSERT INTO hosts (first_name,last_name, contact_number, email) VALUES ('Bilbo', 'Baggins', '0789 123 8765', 'bilbob59@hobbitmail.org');
INSERT INTO hosts (first_name,last_name, contact_number, email) VALUES ('Mario', 'Mario', '0800 100 400', 'mario@warioland.com');

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) VALUES('Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://test', 5, '01/04/2025-22/09/2025', '', 1);
INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) VALUES('Toad House', 'Mario World', 1, 'House', 50.00, 'Description 2', 'https://test', 3, '01/04/2025-22/09/2025', '', 2);
INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) VALUES('Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://test', 5, '01/04/2025-22/09/2025', '', 1);

