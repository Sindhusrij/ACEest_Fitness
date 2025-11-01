from ACEest_Fitness import app

def test_home_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["status"] == "running"

def test_members_route():
    client = app.test_client()
    response = client.get('/members')
    assert response.status_code == 200
    data = response.get_json()
    assert "members" in data
    assert isinstance(data["members"], list)

