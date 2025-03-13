from lib.users.user import User

"""user constructs with fist_name, last_name, email, contact_number and password"""


def test_user_constructs():
    user = User(1, "john", "doe", "johndoe@gmail.com", "080 123 4567", "testpassword")
    assert user.id == 1
    assert user.first_name == "john"
    assert user.last_name == "doe"
    assert user.email == "johndoe@gmail.com"
    assert user.contact_number == "080 123 4567"
    assert user.password == "testpassword"


def test_users_equality():
    user1 = User(1, "john", "doe", "johndoe@gmail.com", "080 123 4567", "testpassword")
    user2 = User(1, "john", "doe", "johndoe@gmail.com", "080 123 4567", "testpassword")
    assert user1 == user2


def test_user_stringifys():
    user1 = User(1, "john", "doe", "johndoe@gmail.com", "080 123 4567", "testpassword")
    assert (
        str(user1)
        == "User(1, john, doe, johndoe@gmail.com, 080 123 4567, testpassword)"
    )
