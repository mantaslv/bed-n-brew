DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    contact_number VARCHAR(20),
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    property_name VARCHAR(255),
    location VARCHAR(255),
    beds INTEGER,
    property_type VARCHAR(255),
    price_per_night NUMERIC(10, 2),
    description TEXT,
    image_url TEXT,
    rating SMALLINT,
    availability TEXT,
    booked_dates TEXT,
    host_id INTEGER,
    CONSTRAINT fk_user FOREIGN KEY (host_id)
    REFERENCES users(id) ON DELETE CASCADE
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    space_id INTEGER,
    customer_name TEXT,
    number_of_guests INTEGER,
    preferred_dates TEXT,
    message_to_host TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (space_id) REFERENCES spaces(id)
    );

INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Bilbo', 'Baggins', '0789 123 8765', 'bilbob59@hobbitmail.org', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');
INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Mario', 'Mario', '0800 100 400', 'mario@warioland.com', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');
INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Luke', 'Skywalker', '0208 783 1234', 'notvadersson@jedi.net', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');
INSERT INTO users (first_name, last_name, contact_number, email, password) VALUES ('Rubeus', 'Hagrid', '0207 934 0232', 'keeperofkeys@hogwarts.edu', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.');

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id)
	VALUES('Bag End', 'Hobbiton', 9, 'House', 289.50, 'Step into the heart of the Shire and experience the timeless charm of Bag End. This cozy, 
    underground hobbit home offers the perfect blend of rustic comfort and countryside tranquility. With its warm, inviting hearth, spacious living areas, 
    and enchanting gardens, Bag End provides a peaceful escape into a world of simple pleasures. Whether you''re relaxing by the fire with a second breakfast
    or exploring the rolling hills of the Shire, this charming retreat is the ideal place for hobbits (and non-hobbits) looking to unwind. Book your magical 
    stay today and discover the beauty of Middle-earth!', 
	'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 
	5, '01/04/2025-22/09/2025', '', 1);


INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) 
    VALUES('Toad House', 'Mario World', 1, 'House', 50.00, 
    'Looking for a whimsical escape? The Toad House in the heart of Mario World offers a charming, cozy retreat full of character and fun. 
    With its bright colors, mushroom-shaped architecture, and inviting atmosphere, this quaint hideaway is perfect for adventurers and families alike.
    Enjoy a restful stay with all the comforts you need, nestled in a lively, colorful environment. Whether you''re relaxing or planning your next adventure,
    the Toad House is the ideal place to recharge. Book your magical stay now and step into a world of wonder!', 
    'https://mario.wiki.gallery/images/e/e1/Toadhousesm3dl.png', 3, '01/04/2025-22/09/2025', '', 2 );

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) 
    VALUES('Yoda''s Hut', 'Dagobah', 2, 'House', 21.99, 'Escape to a tranquil sanctuary on the remote swamps of Dagobah in this legendary retreat. 
    Yoda''s Hut offers a unique, serene getaway where you can unwind in harmony with nature. Surrounded by misty swamps and dense jungle, this humble, 
    yet cozy dwelling provides a perfect spot for reflection, meditation, and quiet relaxation. Experience the wisdom of the Jedi in this secluded haven, 
    complete with simple comforts and a peaceful atmosphere. Whether you seek rest or enlightenment, Yoda''s Hut is the ideal place to reconnect with your inner force.
    Book your unforgettable stay today!',
    'https://lumiere-a.akamaihd.net/v1/images/yodas-hut_a3d1133d.jpeg?region=0%2C75%2C1560%2C880', 1, '01/7/2025-01/10/2025', '', 3 );

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id)  
	VALUES ('Cantina Suite', 'Mos Eisley, Tatooine', 2, 'Hotel', 150.00,  
	'Cozy desert hideaway above a lively cantina. Perfect for smugglers, bounty hunters, and those who "don''t like you" (but we won''t tell). Comes with a free blue milk at check-in.',  
	'https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTIzNjkzMzMxMTk5MDkyOTc5OA%3D%3D/original/97a00231-9378-4b36-ae77-69ea1be3af21.jpeg?im_w=720&im_format=avif', 4, '01/01/2025-31/12/2025', '', 3);

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) 
    VALUES('Hagrid''s Hut', 'Hogwarts Castle', 1, 'House', 33.99, 'Step into a magical hideaway in the heart of the Forbidden Forest. Hagrid''s Hut offers a warm, rustic atmosphere with enchanting views and a welcoming vibe.'
    'This cozy, one-bedroom cottage features a crackling fire, unique décor, and a lush, secluded garden perfect for stargazing or enjoying a quiet afternoon. Ideal for anyone looking to escape the ordinary and experience a truly magical stay.'
    'Perfect for nature lovers and those seeking a touch of wizardry. Book your enchanted getaway today!', 'https://contentful.harrypotter.com/usf1vwtuqyxm/GnhBEt0o1DbE2T3Q7wtpm/9d1ed0f163a12a506271e823a8a86dac/hagrids-hut_1_1800x1248.png', 2, '01/6/2025-01/11/2025', '', 4);

INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id)  
	VALUES ('The Shrieking Shack Penthouse Apartment', 'Hogsmeade, Scotland', 1, 'Flat', 99.00,  
	'The most haunted house in Britain! A charmingly decrepit getaway for those who enjoy eerie noises, creaky floors, and the occasional werewolf. No refunds for paranormal activity.',  
	'https://blockwarts.org/wp-content/uploads/2021/09/cb352102138413cfc51a4e758441a5f0.png?w=751', 3, '01/10/2025-31/10/2025', '', 4);
