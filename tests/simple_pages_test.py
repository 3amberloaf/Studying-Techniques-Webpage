"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/about"' in response.data
    assert b'href="/Pomodoro"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_pomodoro(client):
    """This makes the pomodoro page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Pomodoro" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/Pomodoro")
    assert response.status_code == 200
    assert b"Pomodoro" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404