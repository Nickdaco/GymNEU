from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException



link = 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=8dCpAXZOtNUwCu7Xw7lFdvnMLXWJvC%2fXnljDAys%2fqmQx5OHc0kgRwku22rLLnqz9V187%2fQc5LcOubs4EolABUmZFwTbc8EyCREjolwr1Ekq69xl3QSidow%3d%3d#dailyContainer'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)
click1 = driver.find_element(By.XPATH, '//*[@id="browse-tabs"]/li[1]/a')
click1.click()

wait = WebDriverWait(driver, 10)
try:
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="eventResults"]/div/div[6]/div/div/div/table/tbody/tr[1]/td[1]')))
    event_results = driver.find_element(By.ID, 'eventResults').text
except TimeoutException:
    event_results = "No Events Today"

print(event_results)
