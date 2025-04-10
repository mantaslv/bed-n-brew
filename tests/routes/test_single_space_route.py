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
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    page.goto(f"http://{test_web_address}/spaces/1")
    print(page.content())

    space_image = page.locator(".single-space-item img.space-image")
    expect(space_image).to_have_attribute("src", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Baggins_residence_%27Bag_End%27_with_party_sign.jpg/2880px-Baggins_residence_%27Bag_End%27_with_party_sign.jpg")
    expect(space_image).to_be_visible()
    
    # Check space details
    space_details = page.locator(".single-space-item .space-details")
    header = space_details.locator(".page-header")
    expect(header).to_have_text("Bag End")
    expect(space_details).to_contain_text("House in Hobbiton")
    expect(space_details).to_contain_text("£289.50 per night")
    expect(space_details).to_contain_text("9 beds")
    
    stars = space_details.locator(".star")
    assert stars.count() == 5
    
    space_description = page.locator(".single-space-item .space-description")
    expect(space_description).to_contain_text('Description 1')



