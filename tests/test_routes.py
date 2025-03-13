from playwright.sync_api import Page, expect

"""
When we /GET /spaces
We get a 200 OK response 
"""


def test_route_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/spaces_library.sql")
    response = web_client.get("/spaces")
    assert response.status_code == 200


"""
When we /GET/ spaces/new
We get a 200 OK response
"""


def test_route_spaces_new(db_connection, web_client):
    db_connection.seed("seeds/spaces_library.sql")
    response = web_client.get("/spaces/new")
    assert response.status_code == 200


"""
When we go to '/' we are redirected to the '/spaces' page"""


def test_redirect(db_connection, page, test_web_address):
    db_connection.seed("seeds/spaces_library.sql")
    page.goto(f"http://{test_web_address}/")
    expect(page).to_have_url(f"http://{test_web_address}/spaces")


# ==================== /spaces/new route ====================


def test_create_new_space_form_exists(page, test_web_address):
    # Go to the /space/new page
    page.goto(f"http://{test_web_address}/spaces/new")

    # Check header text
    header_h1 = page.locator("h1")
    expect(header_h1).to_have_text("Create New Space")

    # Ensure that the form exists
    form = page.locator("form")
    expect(form).to_be_visible()


def test_create_new_space(page, test_web_address):
    # Go to the /space/new page
    page.goto(f"http://{test_web_address}/spaces/new")

    # Fill out the form
    page.fill("input[name=property_name]", "london flat")
    page.fill("input[name=price_per_night]", "30")
    page.fill("input[name=beds]", "2")
    page.fill("input[name=location]", "london")
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

    # Check that we're redirected back to the /spaces page
    expect(page).to_have_url(f"http://{test_web_address}/spaces")

    # Check space details
    space_details = page.locator(".space-item .space-details").first
    expect(space_details).to_contain_text("Cozy London Loft")
    expect(space_details).to_contain_text("£120.5 per night")
    expect(space_details).to_contain_text("2 beds")
    expect(space_details).to_contain_text("London, UK")
    expect(space_details).to_contain_text("Rating: 4")
    expect(space_details).to_contain_text("Type: flat")
