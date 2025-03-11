class Space():
    def __init__(self, id, property_name, price_per_night, beds, location, rating, image_url, property_type, description, availability, booked_dates, host_id):
        self.id = id
        self.property_name = property_name
        self.price_per_night = price_per_night
        self.beds = beds
        self.location = location
        self.rating = rating
        self.image_url = image_url
        self.property_type = property_type
        self.description = description
        self.availability = availability
        self.booked_dates = booked_dates
        self.host_id = host_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.property_name}, {self.price_per_night}, {self.beds}, {self.location}, {self.rating}, {self.image_url}, {self.property_type}, {self.description}, {self.availability}, {self.booked_dates}, {self.host_id})"