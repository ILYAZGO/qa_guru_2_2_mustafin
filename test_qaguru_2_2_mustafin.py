from selene.support.shared import browser
from selene import be, have
import pytest

@pytest.fixture()
def browser_config():
    browser.config.window_width=1280
    browser.config.window_height=768
    browser.open('https://google.com/ncr')
    yield
    print("Tests done")

def test_google_should_find_selene(browser_config):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_should_not_find_selene(browser_config):
    browser.element('[name="q"]').should(be.blank).type('randomtext').press_enter()
    browser.element('[id="search"]').should_not(have.text('Selene - User-oriented Web UI browser tests in Python'))