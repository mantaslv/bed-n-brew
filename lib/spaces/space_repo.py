from lib.spaces.space import Space, HostContact

class SpaceRepo():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            space = Space(row["id"], row["property_name"], row["location"], row["beds"], row["property_type"], row["price_per_night"], row["description"], row["image_url"], row["rating"], row["availability"], row["booked_dates"], row["host_id"])
            spaces.append(space)
        return spaces
    
    def find_by_id(self, id):
        spaces = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        space = spaces[0]
        space_object =  Space(space["id"], space["property_name"], space["location"], space["beds"], space["property_type"], space["price_per_night"], space["description"], space["image_url"], space["rating"], space["availability"], space["booked_dates"], space["host_id"])
        
        hosts = self._connection.execute('SELECT * FROM hosts WHERE id = %s', [space_object.host_id])
        host = hosts[0]

        host_object = HostContact(host["id"], host["first_name"], host["last_name"], host["contact_number"], host["email"])
        return space_object, host_object

    def create(self, space):
        self._connection.execute(
            'INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            [space.property_name, space.location, space.beds, space.property_type, space.price_per_night, space.description, space.image_url, space.rating, space.availability, space.booked_dates, space.host_id]
        )
        return None