"""
When we /GET /register
We get a 200 OK response 
"""
def test_register_route(db_connection, web_client):
    db_connection.seed("seeds/tests/users_test_seed.sql")
    response = web_client.get("/register")
    assert response.status_code == 200

"""
When we /GET /register
We get a 200 OK response 
"""
def test_login_route(db_connection, web_client):
    db_connection.seed("seeds/tests/users_test_seed.sql")
    response = web_client.get("/login")
    assert response.status_code == 200