from playwright.sync_api import Page, expect


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
