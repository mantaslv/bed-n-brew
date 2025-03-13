from lib.users.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = User(
                row["id"],
                row["first_name"],
                row["last_name"],
                row["email"],
                row["contact_number"],
                row["password"],
            )
            users.append(user)
        return users

    def find_by_id(self, id):
        users = self._connection.execute("SELECT * From users where id= %s", [id])
        user = users[0]
        return User(
            user["id"],
            user["first_name"],
            user["last_name"],
            user["email"],
            user["contact_number"],
            user["password"],
        )

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users (first_name, last_name, email, contact_number, password) VALUES (%s, %s, %s, %s, %s)",
            [
                user.first_name,
                user.last_name,
                user.email,
                user.contact_number,
                user.password,
            ],
        )
        return None
