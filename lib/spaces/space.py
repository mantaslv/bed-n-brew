class Space():
    def __init__(self, id, property_name, location, beds, property_type, price_per_night, description, image_url, rating, availability, booked_dates, host_id):
        self.id = id
        self.property_name = property_name
        self.location = location
        self.beds = beds
        self.property_type = property_type
        self.price_per_night = price_per_night
        self.description = description
        self.image_url = image_url
        self.rating = rating
        self.availability = availability
        self.booked_dates = booked_dates
        self.host_id = host_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.property_name}, {self.location}, {self.beds}, {self.property_type}, {self.price_per_night}, {self.description}, {self.image_url}, {self.rating}, {self.availability}, {self.booked_dates}, {self.host_id})"

class HostContact():
    def __init__(self, id, first_name, last_name, contact_number, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.contact_number = contact_number
        self.email = email
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"HostContact({self.id}, {self.first_name}, {self.last_name}, {self.contact_number}, {self.email})"