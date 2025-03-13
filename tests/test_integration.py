from playwright.sync_api import Page, expect
from lib.spaces.space import *
from lib.spaces.space_repo import *

"""
Test that list_of_spaces.html template renders with all the information in the database
"""


def test_get_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/spaces_library.sql")

    # Check header text
    page.goto(f"http://{test_web_address}/spaces")
    print(page.content())
    header_h1 = page.locator(".page-header h1")
    expect(header_h1).to_have_text("Available Spaces")

    #     # Check paragraph text
    #     header_p = page.locator(".page-header p")
    #     expect(header_p).to_have_text("Look at these wonderful spaces to rent...")

    # Check space details
    space_details = page.locator(".space-item .space-details").first
    expect(space_details).to_contain_text("Bag End")
    expect(space_details).to_contain_text("£289.50 per night")
    expect(space_details).to_contain_text("9 beds")
    expect(space_details).to_contain_text("Hobbiton")
    expect(space_details).to_contain_text("House")
    stars = space_details.locator(".star")
    assert stars.count() == 5


# ==================== /spaces/new route ====================

"""
Tests that form to create a new space can be submitted 
"""


def test_create_new_space_form_exists(page, test_web_address):
    # Go to the /space/new page
    page.goto(f"http://{test_web_address}/spaces/new")

    # Check header text
    header_h1 = page.locator("h1")
    expect(header_h1).to_have_text("Create New Space")

    # Ensure that the form exists
    form = page.locator("form")
    expect(form).to_be_visible()


def test_create_new_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/spaces_library.sql")

    # Go to the /space/new page
    page.goto(f"http://{test_web_address}/spaces/new")

    # Fill out the form
    page.fill("input[name=property_name]", "london flat")
    page.fill("input[name=price_per_night]", "30")
    page.fill("input[name=beds]", "2")
    page.fill("input[name=location]", "London")
    page.fill(
        "input[name=image_url]",
        "https://images.prismic.io/tembo/Zwff6YF3NbkBXMYy_semidetachedhouseuk.jpg",
    )
    page.locator("[name=property_type]").select_option("House")
    page.fill("input[name=rating]", "5")
    page.fill("#description", "cosy london apartment")
    page.check("#availability")
    page.fill("input[name=host_name]", "Bill")
    page.click("text=Submit")

    #     # Check that we're redirected back to the /spaces page
    #     expect(page).to_have_url(f"http://{test_web_address}/spaces")

    # Now check that the new space is added to the /spaces route
    space_details = page.locator(".space-item .space-details").last
    expect(space_details).to_contain_text("london flat")
    expect(space_details).to_contain_text("£30.00 per night")
    expect(space_details).to_contain_text("2 beds")
    expect(space_details).to_contain_text("House in London")
    stars = space_details.locator(".star")
    assert stars.count() == 5
