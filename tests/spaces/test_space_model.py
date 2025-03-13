from lib.spaces.space import *
"""
Testing space model
Instantiates with:
- id
- property_name
- price_per_night
- beds
- location
- rating
- image_url
- property_type
- description
- availability
- booked_dates
- host_id
"""
def test_instantiates_with_params():
    new_space = Space(1, "Property Name 1", "London", 2, 'House', 289.50, 'Description 1', 'http://test', 5, '01/04/2025-22/09/2025', '', 1)
    assert new_space.id == 1
    assert new_space.property_name == "Property Name 1"
    assert new_space.location == "London"
    assert new_space.beds == 2
    assert new_space.property_type == "House"
    assert new_space.price_per_night == 289.50
    assert new_space.description == "Description 1"
    assert new_space.image_url == "http://test"
    assert new_space.rating == 5
    assert new_space.availability == "01/04/2025-22/09/2025"
    assert new_space.booked_dates == ""
    assert new_space.host_id == 1

def test_instances_are_equal():
    new_space1 = Space(1, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://test', 5, '01/04/2025-22/09/2025', '', 1)
    new_space2 = Space(1, 'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://test', 5, '01/04/2025-22/09/2025', '', 1)
    assert new_space1 == new_space2

def test_object_prints_nicely():
    new_space1 = Space(1,'Bag End', 'Hobbiton', 9, 'House', 289.50, 'Description 1', 'https://test', 5, '01/04/2025-22/09/2025', '', 1)
    assert str(new_space1) == "Space(1, Bag End, Hobbiton, 9, House, 289.50, Description 1, https://test, 5, 01/04/2025-22/09/2025, , 1)"

"""
Testing host contact model
Instantiates with:
- id
- first_name
- last_name
- contact_number
- email
"""

def test_host_instantiates_with_contact_detail_params():
    host_contact = HostContact(5, 'mrs','test', '0789 123 8765','test@email.com')
    assert host_contact.id == 5
    assert host_contact.first_name == 'mrs'
    assert host_contact.last_name == 'test'
    assert host_contact.contact_number == '0789 123 8765'
    assert host_contact.email == 'test@email.com'

def test_host_instances_are_equal():
    host_contact1 = HostContact(5, 'mrs','test', '0789 123 8765','test@email.com')
    host_contact2 = HostContact(5, 'mrs','test', '0789 123 8765','test@email.com')
    assert host_contact1 == host_contact2

def test_host_object_prints_nicely():
    host_contact = HostContact(5, 'mrs','test', '0789 123 8765','test@email.com')
    assert str(host_contact) == "HostContact(5, mrs, test, 0789 123 8765, test@email.com)"