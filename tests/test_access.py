from selenium import webdriver

def test_main_page(browser):
    browser.get("https://www.meetup.com/")
    print(browser.title)
    assert browser.title == "Meetup - We are what we do"