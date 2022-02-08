from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class SiteData:
    def __init__(self, url, find_path, find_type, title):
        self.url = url
        self.find_path = find_path
        self.find_type = find_type
        self.title = title
        self.data = None

    # Takes URL, element path, type of find -> Returns List of Web Elements
    def scrape_site(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)

        if self.find_type.lower() == 'class_name':
            return driver.find_elements(By.CLASS_NAME, self.find_path)
        elif self.find_type.lower() == 'xpath':
            return driver.find_elements(By.XPATH, self.find_path)
        else:
            print("unable to find anything")
            