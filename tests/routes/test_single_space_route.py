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


def test_booking_space_form_exists(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/{id}")
    book_now_button = page.locator("label[for='booking-modal-toggle']")
    expect(book_now_button).to_be_visible()
    # Check that the pop up booking form is initially hidden
    modal = page.locator(".modal")
    expect(modal).to_be_hidden()


def test_booking_space_form_submission(page, test_web_address, db_connection):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    page.goto(f"http://{test_web_address}/spaces/{id}") # this will go to the individual space page
    page.click("label[for='booking-modal-toggle']") # this will click the 'Book Now' button at the bottom of the listing
    page.fill("input[name=customer_name]", "John Doe") # this will fill in the booking form fields
    page.fill("input[name=number_of_guests]", "3")
    page.fill("input[name=preferred_dates]", "2025-05-01 to 2025-05-07")
    page.fill("textarea[name=message_to_host]", "Looking forward to the stay!")
    user_id = page.locator("input[name=user_id]").get_attribute("value") # this will get the user_id from the hidden input field
    expect(user_id).to_be_non_empty() # this will check that the user_id is not empty
    page.click("button[type=submit]") 
    flash_message = page.locator(".alert.alert-success") # this will check that the flash message is visible
    expect(flash_message).to_be_visible()
    expect(flash_message).to_have_text("Your booking request has been sent to the host!")
    expect(page).to_have_url(f"http://{test_web_address}/spaces/{id}")