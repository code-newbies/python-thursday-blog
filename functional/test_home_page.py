import pytest
from selenium import webdriver

@pytest.fixture
def browser(request):
    browser = webdriver.Firefox()
    def tearDown():
        browser.quit()
    request.addfinalizer(tearDown)
    return browser

def test_page_loads(browser):
    browser.get('http://localhost:8000')
    assert 'Python Thursday Blog' in browser.title

def test_posts_loads(browser):
	browser.get('http://localhost:8000')
	assert 'Python Thursday Blog - Posts' in browser.title


