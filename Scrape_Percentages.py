from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_site(site, path, type):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site)
    if type.lower() == 'class_name':
        return WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, path)))
    if type.lower() == 'xpath':
        return WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, path)))
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

sport_court_link = 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=2sdeuuZ3cxh0hVZgJYA84txwBAjutRyjhYavKNQt%2f1ZU02OX1qeFfxh8QvnmqjnnvPoiPyTnIl8ZtHpxkgfPUK6dvglR7G8DdxFP69QIaS4hyDGPHot7LbGnj5jMFpqD'
court_2_link = 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=8dCpAXZOtNUwCu7Xw7lFdvnMLXWJvC%2fXnljDAys%2fqmQx5OHc0kgRwku22rLLnqz9V187%2fQc5LcOubs4EolABUmZFwTbc8EyCREjolwr1Ekq69xl3QSidow%3d%3d'
court_3_link = 'https://nuevents.neu.edu/CustomBrowseEvents.aspx?data=pw7uNs6e9v8qbfdIsvc5fDYq1MFunilYcWUxDMrP56yKqAjIwwaKA11U%2fQckiFjB2tWbX%2fc8606fDHS3t5PPuSnrcoE8cTQGmAOsO4wdf4ZaUfDtNt1OGQ%3d%3d'

#navigates to daily view and returns events of that day.
def scrape_calendar(site):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(site)
    daily_view = driver.find_element(By.XPATH, '//*[@id="browse-tabs"]/li[1]/a')
    daily_view.click()
    try:
        return WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'event-grid')))
    except:
        return []

#converts daily events to list of events.
sport_court_events = [event.text for event in scrape_calendar(sport_court_link)]
court_2_events = [event.text for event in scrape_calendar(court_2_link)]
court_3_events = [event.text for event in scrape_calendar(court_3_link)]

for i in range(len(sport_court_events)):
    sport_court_events[i] = sport_court_events[i].split(' Marino Center')[0]
for i in range(len(court_2_events)):
    court_2_events[i] = court_2_events[i].split(' Marino Center')[0]
for i in range(len(court_3_events)):
    court_3_events[i] = court_3_events[i].split(' Marino Center')[0]

print(court_3_events, court_2_events, sport_court_events)
court_info_dict = {'Start Time': None, 'End Time': None, 'Event': None}


#['5:30 AM 12:00 AM ET Open Basketball'] 
#['5:30 AM 12:00 AM ET Open Basketball']
#['5:45 AM 1:45 PM ET Open Roller Hockey', '2:00 PM 5:45 PM ET Open Volleyball', '6:00 PM 8:00 PM ET Wrestling (Club Sports)']


#puts whole list of dict in json
with open("gym_percents.json", "w") as outfile: 
    json.dump(marino_info, outfile)
