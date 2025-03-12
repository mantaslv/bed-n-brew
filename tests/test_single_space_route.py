from playwright.sync_api import Page, expect

"""
When we send GET /spaces/<1>
We see:
- property_name
- price_per_night
- beds
- location
- rating
- image_url
- property_type
- description
- availability
- host_id(links to):
	- name
    - contact_number
    - email
"""
def test_get_space_1(page, test_web_address, db_connection):
    db_connection.seed("seeds/spaces_library.sql")
    page.goto(f"http://{test_web_address}/spaces/1")
    
    space_image = page.locator(".space-item img.space-image")
    expect(space_image).to_have_attribute("src", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg")
    expect(space_image).to_be_visible()
    
    # Check space details
    space_details = page.locator(".space-item .space-details")
    header = space_details.locator(".page-header")
    expect(header).to_have_text("Bag End")
    expect(space_details).to_contain_text(["289.5" "9" "Hobbiton" "✰✰✰✰✰" "House"])
    
    space_description = page.locator(".space-item .space-description")
    expect(space_description).to_have_text(
		"""
			Step into the heart of the Shire and experience the timeless charm of Bag End. This cozy, 
			underground hobbit home offers the perfect blend of rustic comfort and countryside tranquility. With its warm, inviting hearth, spacious living areas, 
			and enchanting gardens, Bag End provides a peaceful escape into a world of simple pleasures. Whether you''re relaxing by the fire with a second breakfast
			or exploring the rolling hills of the Shire, this charming retreat is the ideal place for hobbits (and non-hobbits) looking to unwind. Book your magical 
			stay today and discover the beauty of Middle-earth!
		"""
	)
