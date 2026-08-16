from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

from app.pages.vendor_page import VendorPage

from app.models.vendor_model import VendorModel


class BrowserTool:

    def browse(self, url):

        driver = webdriver.Chrome(

            service=Service(

                ChromeDriverManager().install()

            )

        )

        driver.maximize_window()

        page = VendorPage(driver)

        page.open(url)

        vendor = VendorModel(

            company_name=page.get_page_title().split("-")[0].strip(),

            website=page.get_current_url(),

            page_title=page.get_page_title(),

            privacy_policy=page.has_privacy_policy(),

            contact_page=page.has_contact_page(),

            https_enabled=page.get_current_url().startswith("https")

        )

        driver.quit()

        return vendor.model_dump()