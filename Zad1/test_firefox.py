import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Firefox(executable_path='C:/Users/sleman/Testowanie automatyczne/laboratorium-15-tusiaa/Firefox/geckodriver')
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        # driver.find_element()
        driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        driver.find_element_by_id("search_button_homepage").submit()
        self.assertEqual(driver.title, "DuckDuckGo — Privacy, simplified.")
        driver.quit()


if __name__ == '__main__':
    unittest.main()