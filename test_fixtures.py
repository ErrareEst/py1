import pytest


@pytest.fixture
def browser(scope="session"):
    print("launching browser")
    yield
    print("closing browser")

@pytest.fixture
def login_page(browser):
    print("launching login page")
    pass

@pytest.fixture
def user():
    print("creating user")
    return "username", "password"

def test_login(login_page,user):
    username,password = user
    assert username == "username"
    assert password == "password"