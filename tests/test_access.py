
meetup_homepage_url = "https://www.meetup.com/"
import pdb

def test_title(browser):
    browser.get(meetup_homepage_url)
    assert browser.title == "Meetup - We are what we do"

    # - banner text
    # - boxes with images and meetup category names
    # - join meetup button
    # - top header login/sign up
    # - search box
def test_homepage(browser):
    browser.get(meetup_homepage_url)
    headers = browser.find_elements_by_css_selector('main h1')
    assert len(headers) == 1

    header = headers[0]
    assert len(header.text) > 2
