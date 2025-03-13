from lib.users.user_repo import UserRepository
from lib.users.user import User


"""
Test user repository gets all records
"""
def test_all_method_gets_all(db_connection):
    db_connection.seed("seeds/tests/users_test_seed.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, 'Bilbo', 'Baggins', 'bilbob59@hobbitmail.org', '0789 123 8765', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.'),
        User(2, 'Mario', 'Mario', 'mario@warioland.com', '0800 100 400', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.'),
    ]

"""
When UserRepository called with #find_by_id method
And id passed as a parameter
It returns a User object with that id and reflects the seed data 
"""
def test_find_by_id_method(db_connection):
    db_connection.seed("seeds/tests/users_test_seed.sql")
    repo = UserRepository(db_connection)
    user = repo.find_by_id(1)
    assert user == User(
        1, 'Bilbo', 'Baggins', 'bilbob59@hobbitmail.org', '0789 123 8765', '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.'
    )


"""
When UserRepository called with #create
And user object passed as parameter
Creates a new record in the database with all the information
"""
def test_create_creates_new_db_entry(db_connection):
    db_connection.seed("seeds/tests/users_test_seed.sql")
    repo = UserRepository(db_connection)
    repo.create(
        User(
            None,
            "Sarah",
            "Parker",
            "SarahParker@gmail.com",
            "010 678 1234",
            "mypassword456",
        )
    )
    result = repo.all()
    assert result == [
        User(1, 'Bilbo', 'Baggins', 'bilbob59@hobbitmail.org','0789 123 8765',  '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.'),
        User(2, 'Mario', 'Mario', 'mario@warioland.com','0800 100 400',  '$2b$12$eD4USQ4Mgd7RUc88c9UqOe6oddbqnVlXDqgguOrLtVESjpbRqUn2.'),
        User(3, "Sarah", "Parker", "SarahParker@gmail.com", "010 678 1234", "mypassword456",),
    ]