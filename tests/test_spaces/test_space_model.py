from lib.spaces.space import *

"""
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
    new_space = Space(1, "Property Name 1", 300, 2, "London", 5, "http://testURL", "Flat", "VERY nice flat", "11/03/2025 - 14/03/2025", "15/03/2025, 16/03/2025", 1)
    assert new_space.id == 1
    assert new_space.property_name == "Property Name 1"
    assert new_space.price_per_night == 300
    assert new_space.beds == 2
    assert new_space.location == "London"
    assert new_space.rating == 5
    assert new_space.image_url == "http://testURL"
    assert new_space.property_type == "Flat"
    assert new_space.description == "VERY nice flat"
    assert new_space.availability == "11/03/2025 - 14/03/2025"
    assert new_space.booked_dates == "15/03/2025, 16/03/2025"
    assert new_space.host_id == 1