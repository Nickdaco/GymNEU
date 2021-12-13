from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json


def scrape_site(site, path, type):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site)
    if type.lower() == 'class_name':
        return driver.find_elements(By.CLASS_NAME, path)
    if type.lower() == 'xpath':
        return driver.find_elements(By.XPATH, path)
    driver.close()

#grabs percentages
availability_perc = scrape_site("https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7", "circleChart", 'class_name')

gym_list = [
    'Marino Center - 2nd Floor',
    'Marino Center - Gymnasium',
    'Marino Center - 3rd Floor Weight Room',
    'Marino Center - 3rd Floor Select & Cardio',
    'Marino Center - Track',
    'SquashBusters - 4th Floor']

#creates dictionary with name of component of gym as key, and an integer representing percent full as value.
percent_list = [int(percent.text[0:-1]) for percent in availability_perc]
gym_percents = dict(zip(gym_list, percent_list))


#grabs operating hours
operating_hours_days = scrape_site("https://www.northeastern.edu/campusrec/", "/html/body/section[2]/div/header/table/tbody/tr/th[1]/p[2]", "xpath")

#turns string into single item list.
days_hours = [item.text for item in operating_hours_days]

#takes single item list and divides into new list at line breaks.
days_hours = days_hours[0].split('\n')

#initialize dictonary key and value.
open_date = []
open_hours = []

#create separate lists of dates and times.
for elem in days_hours:
    open_date.append(elem.split(': ')[0])
    open_hours.append(elem.split(': ')[1])

#combine lists of dates and times into dict.
open_date_hours = dict(zip(open_date, open_hours))

#combines dict of open hours and dict of percent full values into one list.
marino_info = [gym_percents, open_date_hours]

#puts whole list of dict in json
with open("gym_percents.json", "w") as outfile:
    json.dump(marino_info, outfile)
