
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

    category_cards = browser.find_elements_by_css_selector('[data-testid="category-card"]')
    assert len(category_cards) > 1

    for card in category_cards:
        img = card.find_element_by_css_selector('img')
        assert img is not None

        image_was_loaded = browser.execute_script(
           "return arguments[0].complete && "+
            "typeof arguments[0].naturalWidth != \"undefined\" && "+
            "arguments[0].naturalWidth > 0", img)


        assert image_was_loaded is True, img.get_attribute('src')

