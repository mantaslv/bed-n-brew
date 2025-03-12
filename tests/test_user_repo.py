from lib.users.user_repo import UserRepository
from lib.users.user import User


"""
Test user repository gets all records
"""
def test_all_method_gets_all(db_connection):
    db_connection.seed("seeds/users_table.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert users == [
        User(1, "John", "Smith", "JohnSmith@gmail.com", "010 034 4455", "password123"),
        User(2, "Amy", "Ryan", "AmyRyan@outlook.com", "010 033 8274", "snow755"),
        User(
            3, "Callum", "Brown", "CallumBrown@icloud.com", "010 374 2174", "football12"
        ),
        User(
            4, "Emma", "Johnson", "EmmaJohnson@gmail.com", "010 456 7890", "secure123"
        ),
    ]


"""
When UserRepository called with #find_by_id method
And id passed as a parameter
It returns a User object with that id and reflects the seed data 
"""
def test_find_by_id_method(db_connection):
    db_connection.seed("seeds/users_table.sql")
    repo = UserRepository(db_connection)
    user = repo.find_by_id(1)
    assert user == User(
        1, "John", "Smith", "JohnSmith@gmail.com", "010 034 4455", "password123"
    )


"""
When UserRepository called with #create
And user object passed as parameter
Creates a new record in the database with all the information
"""
def test_create_creates_new_db_entry(db_connection):
    db_connection.seed("seeds/users_table.sql")
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
        User(1, "John", "Smith", "JohnSmith@gmail.com", "010 034 4455", "password123"),
        User(2, "Amy", "Ryan", "AmyRyan@outlook.com", "010 033 8274", "snow755"),
        User(3, "Callum", "Brown", "CallumBrown@icloud.com", "010 374 2174", "football12"),
        User(4, "Emma", "Johnson", "EmmaJohnson@gmail.com", "010 456 7890", "secure123"),
        User(5, "Sarah", "Parker", "SarahParker@gmail.com", "010 678 1234", "mypassword456",),
    ]
