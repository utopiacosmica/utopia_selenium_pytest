from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('driver_windows\chromedriver')
driver.maximize_window()


def test_python_org_search():
        driver.get("http://www.python.org")
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        driver.close()
