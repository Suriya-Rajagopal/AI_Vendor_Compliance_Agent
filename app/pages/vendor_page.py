from selenium.webdriver.common.by import By


class VendorPage:

    def __init__(self, driver):

        self.driver = driver

    def open(self, url):

        self.driver.get(url)

    def get_page_title(self):

        return self.driver.title

    def get_current_url(self):

        return self.driver.current_url

    def has_privacy_policy(self):

        links = self.driver.find_elements(By.TAG_NAME, "a")

        for link in links:

            text = link.text.lower()

            if "privacy" in text:
                return True

        return False

    def has_contact_page(self):

        links = self.driver.find_elements(By.TAG_NAME, "a")

        for link in links:

            text = link.text.lower()

            if "contact" in text:
                return True

        return False