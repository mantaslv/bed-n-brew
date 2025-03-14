from playwright.sync_api import expect

"""
When we /GET /spaces
We get a 200 OK response 
"""
def test_route_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    response = web_client.get("/spaces/")
    assert response.status_code == 200

"""
When we /GET/ spaces/new and not logged in
We get a 302 OK response
"""
def test_route_spaces_new(db_connection, web_client):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    response = web_client.get("/spaces/new")
    assert response.status_code == 302

"""
When we go to '/' we are redirected to the '/spaces' page
"""
def test_redirect(db_connection, page, test_web_address):
    db_connection.seed("seeds/tests/spaces_test_seed.sql")
    page.goto(f"http://{test_web_address}/")
    expect(page).to_have_url(f"http://{test_web_address}/spaces/")
