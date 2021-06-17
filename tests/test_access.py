from selenium.webdriver.common.keys import Keys 


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

    forms = browser.find_elements_by_tag_name("form")
    #assert len(forms) == 1
    # TODO: if there are more forms print them out
    # TODO: a better way to locate the form using an id (that it does not have now)
    # len(forms) == 1
    form = forms[0]
    assert form.find_element_by_id("search-keyword-input")
    assert form.find_element_by_id("location-typeahead-searchLocation")
    assert form.find_element_by_css_selector('[data-testid="search-submit"]')

def test_search_form(browser):
    browser.get(meetup_homepage_url)

    form = browser.find_element_by_tag_name("form")
    form.find_element_by_id("search-keyword-input").send_keys("hiking")
    form.find_element_by_id("location-typeahead-searchLocation").send_keys("London, GB") 
    # TODO: make the location selector work, try this:
    # https://stackoverflow.com/questions/28482297/send-keys-not-to-element-but-in-general-selenium
    #form.find_element_by_id("location-typeahead-searchLocation").send_keys(Keys.DOWN)
    form.find_element_by_id("location-typeahead-searchLocation").send_keys(Keys.ENTER)
    assert browser.title == 'Find Events & Groups | Meetup'

    # import code
    # code.interact(local=locals())
    #pdb.set_trace()
    