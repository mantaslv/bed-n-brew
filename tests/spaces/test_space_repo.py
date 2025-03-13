from lib.spaces.space_repo import *
from lib.spaces.space import *

"""
Test space repository gets all records
"""
def test_all_method_gets_all(db_connection):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    repository = SpaceRepo(db_connection)
    listings = repository.all()
    assert listings == [
        Space(1, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 5, '01/04/2025-22/09/2025', '', 1), 
        Space(2, 'Toad House', 'Mario World', 1, 'House', 50.00, 'Description 2', 'https://mario.wiki.gallery/images/e/e1/Toadhousesm3dl.png', 3, '01/04/2025-22/09/2025', '', 2),
        Space(3, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 5, '01/04/2025-22/09/2025', '', 1), 
    ]

"""
When SpaceRepo called with #find_by_id method
And id passed as a parameter
It returns a Space object with that id and reflects the seed data 
"""
def test_find_by_id_method(db_connection):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    repo = SpaceRepo(db_connection)
    space = repo.find_by_id(3)
    space_class = Space(3, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 5, '01/04/2025-22/09/2025', '', 1)
    host_class = HostContact(1, 'Bilbo','Baggins', '0789 123 8765','bilbob59@hobbitmail.org')
    assert space[0] == space_class
    assert space[1] == host_class

"""
When SpaceRepo called with #create
And space object passed as parameter
Creates a new record in the database with all the information
"""

def test_create_creates_new_db_entry(db_connection):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    repo = SpaceRepo(db_connection)
    repo.create(Space(None, 'Mount Doom', 'Mordor', 430, 'Castle', 100000.58, 'Description 3', 'https://test', 4, '01/04/2025-22/09/2025', '', 1))
    result = repo.all()
    expected_spaces = [
        Space(1, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 5, '01/04/2025-22/09/2025', '', 1), 
        Space(2, 'Toad House', 'Mario World', 1, 'House', 50.00, 'Description 2', 'https://mario.wiki.gallery/images/e/e1/Toadhousesm3dl.png', 3, '01/04/2025-22/09/2025', '', 2),
        Space(3, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg', 5, '01/04/2025-22/09/2025', '', 1), 
        Space(4, 'Mount Doom', 'Mordor', 430, 'Castle', 100000.58, 'Description 3', 'https://test', 4, '01/04/2025-22/09/2025', '', 1)
    ]
        
    assert result == expected_spaces
    