import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--head", action='store_true')


@pytest.fixture(scope='session')
def browser(request):
    options = webdriver.ChromeOptions()
    if not request.config.getoption("--head"):
        options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver
    driver.close()