from lib.spaces.space import *

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
        spaces = self._connection.execute('SELECT * From spaces where id= %s', [id])
        space = spaces[0]
        return Space(space["id"], space["property_name"], space["location"], space["beds"], space["property_type"], space["price_per_night"], space["description"], space["image_url"], space["rating"], space["availability"], space["booked_dates"], space["host_id"])
    
    def create(self, space):
        self._connection.execute(
            'INSERT INTO spaces (property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', 
            [space.property_name, space.location, space.beds, space.property_type, space.price_per_night, space.description, space.image_url, space.rating, space.availability, space.booked_dates, space.host_id]
        )
        return None