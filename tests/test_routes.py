from playwright.sync_api import Page, expect


# ====================== /spaces route ======================


def test_visit_spaces_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    # Check header text
    header_h1 = page.locator(".page-header h1")
    expect(header_h1).to_have_text("Available Spaces")

    # Check paragraph text
    header_p = page.locator(".page-header p")
    expect(header_p).to_have_text("Look at these wonderful spaces to rent...")

    # Check space details
    space_details = page.locator(".space-item .space-details").first
    expect(space_details).to_contain_text("Cozy London Loft")
    expect(space_details).to_contain_text("£120.5 per night")
    expect(space_details).to_contain_text("2 beds")
    expect(space_details).to_contain_text("London, UK")
    expect(space_details).to_contain_text("Rating: 4")
    expect(space_details).to_contain_text("Type: flat")


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

    # Now check that the new space is added to the /spaces rout
    space_details = page.locator(".space-item .space-details").last
    expect(space_details).to_contain_text("london flat")
    expect(space_details).to_contain_text("£30.0 per night")
    expect(space_details).to_contain_text("2 beds")
    expect(space_details).to_contain_text("london")
    expect(space_details).to_contain_text("Rating: 5")
    expect(space_details).to_contain_text("Type: house")
